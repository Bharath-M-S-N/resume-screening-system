import streamlit as st
import os
import tempfile
import pandas as pd

from preprocessing import clean_text
from vectorizer import vectorize_text
from similarity import cosine_sim
from pdf_reader import extract_text_from_pdf
from skills import extract_skills, calculate_final_score
from experience import extract_experience_years, experience_bonus

# Streamlit Page Config
st.set_page_config(page_title="Resume Screaning System", layout="centered")

st.title("📄 Resume Screening System")
st.write("Upload a job description and resume to rank candidates.")

st.markdown("---")

# File Uploads
job_file = st.file_uploader(
    "Upload Job Description (TXT)",
    type=["txt"]
    )

resume_files = st.file_uploader(
    "Uplaod Resumes (PDF or TXT)",
    type=["pdf","txt"],
     accept_multiple_files=True
     )

# Helper fuctions

def read_uploaded_txt(file):
    return file.read().decode("utf-8")

def save_uploaded_file(uploaded_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

# Run Analsis
if st.button("Analyze Resumes"):

    if job_file is None or not resume_files:
        st.error("Please upload a job description and at least one resume.")
        st.stop()

    # Read and clean job description
    job_text = read_uploaded_txt(job_file)
    clean_job = clean_text(job_text)

    resumes = []
    resumes_names = []

    #Read resumes
    for resume in resume_files:
        if resume.name.endswith(".pdf"):
            path = save_uploaded_file(resume)
            raw_text = extract_text_from_pdf(path)
        else:
            raw_text = read_uploaded_txt(resume)

        cleaned_text = clean_text(raw_text)
        resumes.append(cleaned_text)
        resumes_names.append(resume.name)

    # TF-IDF Vectorization
    all_texts = resumes + [clean_job]
    tfidf_matrix = vectorize_text(all_texts)
    job_vector = tfidf_matrix[-1]

    results = []

    # Scoring pipeline
    for i in range(len(resumes)):
        cosine_score = cosine_sim(tfidf_matrix[i], job_vector)
        skills_matched = extract_skills(resumes[i])
        years = extract_experience_years(resumes[i])
        exp_bonus = experience_bonus(years)
        skill_score = calculate_final_score(cosine_score, skills_matched)
        final_score = skill_score + exp_bonus

        results.append({
            "Resume": resumes_names[i],
            "Cosine Score": round(cosine_score,3),
            "Skills Matched": ", ".join(skills_matched),
            "Experience (Years)": years,
            "Final Score": round(final_score, 3)
        })

    # Sort results
    results.sort(key=lambda X: X["Final Score"], reverse=True)

    st.success("Analysis Complete!")

    st.markdown("## 📊 Resume Ranking Results")
    df = pd.DataFrame(results)

    # Make serail start from 1
    df.index = df.index + 1

    st.dataframe(df, use_container_width=True)

