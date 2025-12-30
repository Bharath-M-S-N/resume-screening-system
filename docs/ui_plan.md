# UI Plan – Resume Screening System

## Objective

The objective of adding a UI is to convert the Resume Screening System
into a user-friendly web application that can be accessed through a browser.

This allows recruiters or users to upload resumes and job descriptions
without interacting directly with the command line.

---

## Proposed Tool

**Streamlit** is chosen for building the UI because:
- It is lightweight and fast to develop
- It integrates easily with Python backends
- It requires minimal frontend knowledge
- It is suitable for ML and NLP demos

---

## User Flow

1. User opens the web application in a browser
2. User uploads:
   - One job description file
   - Multiple resume files (PDF or TXT)
3. User clicks **“Analyze Resumes”**
4. Backend processes the files:
   - Text preprocessing
   - TF-IDF vectorization
   - Similarity scoring
   - Skill and experience scoring
5. Results are displayed:
   - Ranked resumes
   - Final scores
   - Skills matched
   - Experience detected

---

## Backend Integration

The existing Python modules will be reused:
- `preprocessing.py`
- `vectorizer.py`
- `similarity.py`
- `skills.py`
- `experience.py`
- `pdf_reader.py`

No changes are required to the core logic.
The UI will act as a wrapper around the existing pipeline.

---

## Output Display

The UI will show:
- Resume name
- Cosine similarity score
- Matched skills
- Experience in years
- Final score
- Ranking order

Results may be displayed using tables or expandable sections.

---

## Deployment Plan (Future)

The application can be deployed using:
- Streamlit Cloud
- Render
- Hugging Face Spaces

This enables the project to be shared as a SaaS-style demo.

---

## Project Status

UI development is planned but not implemented.
The core resume screening system is complete and functional.
