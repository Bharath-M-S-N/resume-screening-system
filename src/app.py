import streamlit as st

st.set_page_config(page_title="Resume Screening System", layout="centered")

st.title("📄 Resume Screening System")
st.write("Upload a job description and resumes to rank candidates.")

st.markdown("---")

# Job description upload
job_file = st.file_uploader(
    "upload Job Description (TXT only)",
    type=["txt"],
    key="job"
)

# Resume uploads
resume_files = st.file_uploader(
    "Upload Resumes (PDF or TXT)",
    type=["pdf","txt"],
    key="resumes"
)

st.markdown("---")

if st.button("Analyze Resumes"):
    if job_file is None or not resume_files:
        st.error("Please upload a job description and atleast one resume.")
    else:
        st.success("Files uploaded successfully!")
        st.write(f"Job Description file: **{job_file.name}**")
        st.write("Resume uploaded:")
        for r in resume_files:
            st.write(f"- {r.name}")

        st.info("Backend processing will be connected in the next step.")