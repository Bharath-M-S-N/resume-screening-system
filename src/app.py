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
st.set_page_config(page_title="Resume Screaning System", layout="wide")

st.title("📄 Resume Screening System")
st.write("Upload a job description and multiple resumes to rank candidates automatically.")

st.markdown("---")

# Upload section
st.header("📌 Upload Job Description")

# File Uploads
job_file = st.file_uploader(
    "Upload Job Description (TXT or PDF)",
    type=["txt", "pdf"]
    )

st.header("📂 Upload Resumes")

resume_files = st.file_uploader(
    "Uplaod Resumes (PDF or TXT)",
    type=["pdf","txt"],
     accept_multiple_files=True
     )

# Helper fuctions

def read_uploaded_txt(file):
    return file.read().decode("utf-8", errors="ignore")

def save_uploaded_file(uploaded_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

# Run Analsis
process_disabled = not job_file or not resume_files

run_button = st.button(
    "🔍 Rank Resumes",
    disabled=process_disabled
)

if run_button:

    if job_file is None:
        st.warning("Please upload a job description.")
        st.stop()

    if not resume_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    with st.spinner("Analyzing resumes... Please wait ⏳"):

        # Read and clean job description
        if job_file.name.endswith(".pdf"):
            job_path = save_uploaded_file(job_file)
            job_text = extract_text_from_pdf(job_path)
        else:
            job_text = read_uploaded_txt(job_file)

        if job_text.strip() == "":
            st.error("Job description file is empty.")
            st.stop()
    
        clean_job = clean_text(job_text)

        resumes = []
        resumes_names = []

        #Read resumes
        for resume in resume_files:
            try:
                if resume.name.endswith(".pdf"):
                    path = save_uploaded_file(resume)
                    raw_text = extract_text_from_pdf(path)
                else:
                    raw_text = read_uploaded_txt(resume)
                
                if raw_text.strip() == "":
                    st.warning(f"⚠️ {resume.name} is empty and was skipped.")
                    continue

                cleaned_text = clean_text(raw_text)
                resumes.append(cleaned_text)
                resumes_names.append(resume.name)

            except Exception as e:
                st.warning(f"⚠️ Could not read {resume.name}. Skipped.")
                continue

        if not resumes:
            st.error("No valid resumes found to process.")
            st.stop()

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

    st.dataframe(df, width="stretch")

