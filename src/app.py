import streamlit as st
import os
import tempfile
import pandas as pd
import zipfile

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
    "✔️ Upload Job Description (TXT or PDF)",
    type=["txt", "pdf"]
    )

st.header("📂 Upload Resumes")
st.caption("✔️ Upload multiple PDF/txt files **OR** upload a ZIP containing resumes.")

resume_files = st.file_uploader(
    "Uplaod Resumes",
    type=["pdf","txt","zip"],
     accept_multiple_files=True
     )

# Show upload Feedback
if resume_files:
    st.success(f"✅ {len(resume_files)} resume(s) uploaded.")
    with st.expander("📄 View uploaded resume names"):
        for file in resume_files:
            st.write("\u2022", file.name)

# Helper fuctions
def read_uploaded_txt(file):
    return file.read().decode("utf-8", errors="ignore")

def save_uploaded_file(uploaded_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    return file_path

def extract_zip(zip_path):
    extract_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(zip_path,"r") as zip_ref:
        zip_ref.extractall(extract_dir)
    return extract_dir

# Run Analsis
process_disabled = not job_file or not resume_files

run_button = st.button(
    "🔍 Rank Resumes",
    disabled=process_disabled
)

if run_button:

    with st.spinner("⏳ Analyzing resumes, pleses wait..."):

        # Read and clean job description
        if job_file.name.endswith(".pdf"):
            job_path = save_uploaded_file(job_file)
            job_text = extract_text_from_pdf(job_path)
        else:
            job_text = read_uploaded_txt(job_file)

        if job_text.strip() == "":
            st.error("❌ Job description file is empty.")
            st.stop()
    
        clean_job = clean_text(job_text)

        resumes = []
        resumes_names = []

        #Read resumes
        for uploaded in resume_files:

            # ZIP handling
            if uploaded.name.endswith(".zip"):
                zip_path = save_uploaded_file(uploaded)
                extract_dir = extract_zip(zip_path)

                for root, _, files in os.walk(extract_dir):
                    for file in files:
                        file_path = os.path.join(root, file)

                        try:
                            if file.lower().endswith(".pdf"):
                                raw_text = extract_text_from_pdf(file_path)
                            elif file.lower().endswith(".txt"):
                                with open(file_path,"r",encoding="utf-8", errors="ignore") as f:
                                    raw_text = f.read()
                            else:
                                continue

                            if not raw_text.strip():
                                continue

                            resumes.append(clean_text(raw_text))
                            resumes_names.append(file)

                        except Exception:
                            continue

            else:
                try:
                    if uploaded.name.endswith(".pdf"):
                        path = save_uploaded_file(uploaded)
                        raw_text = extract_text_from_pdf(path)
                    else:
                        raw_text = read_uploaded_txt(uploaded)
                    
                    if not raw_text.strip():
                        st.warning(f"⚠️ {uploaded.name} is empty or unreadable and was skipped.")
                        continue

                    cleaned_text = clean_text(raw_text)
                    resumes.append(cleaned_text)
                    resumes_names.append(uploaded.name)

                except Exception:
                    st.warning(f"⚠️ Could not read {uploaded.name}. Skipped.")
                    continue

        if not resumes:
            st.error("❌ No valid resumes found to process.")
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

    # Display results
    st.success("Analysis Complete!")

    st.markdown("## 📊 Resume Ranking Results")
    df = pd.DataFrame(results)

    # Make serail start from 1
    df.index = df.index + 1

    st.dataframe(df, width="stretch")

