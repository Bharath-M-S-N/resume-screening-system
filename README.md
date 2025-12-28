# Resume Screening System

## Project Overview
The Resume Screening System is an NLP-based application that automates the initial screening of resumes by comparing them with a given job description.
It ranks candidates based on textual similarity, skills, and experience to support faster and more accurate hiring decisions.

---

## Problem Statement
Recruiters often receive a large number of resumes for a single job opening, making manual screening time-consuming and inefficient.
This system automates resume evaluation by analyzing textual relevance between resumes and job requirements.

---

## Inputs
- Resume text (PDF or text format)
- Job description text

---

## Outputs
- Similarity score for each resume
- Ranked list of candidates

---

## Project Workflow (Pipeline)

1. Resume and job description texts are collected.
2. Text is preprocessed (lowercasing, removing symbols and stopwords).
3. TF-IDF converts text into numerical vectors.
4. Cosine similarity measures relevance between resumes and job description.
5. Skill-based and experience-based scores are applied.
6. Final scores are generated and resumes are ranked.

---

## Concept Understanding

### Term Frequency (TF)
Shows how often a word appears in a document.
Frequent skills in a resume indicate candidate expertise.

### Inverse Document Frequency (IDF)
Reduces the importance of very common words across resumes while increasing the weight of rare and meaningful terms.

### TF-IDF
Highlights important words that are frequent in a resume but not common across all resumes.

### Cosine Similarity
Measures similarity between two documents based on vector direction.
Value close to 1 means a strong match.
Value close to 0 means a weak match.

### Text Preprocessing
Removes noise and standardizes text before vectorization.

---

## Resume Ranking
The system computes cosine similarity scores and ranks resumes in descending order, with higher scores indicating better matches.

---

## Features
- PDF resume parsing
- Text preprocessing
- TF-IDF vectorization
- Cosine similarity ranking
- Skill-based score boosting
- Experience-based scoring

---



## How to Run

1. Install dependencies  
   pip install -r requirements.txt

2. Run the project  
   python src/main.py

---

## Tech Stack
- Python
- NLP (TF-IDF, Cosine Similarity)
- Regex
- NumPy
- Scikit-learn

---

## Future Improvements
- Add Streamlit web interface
- Improve error handling and logging
- Support multiple job descriptions
- Add machine learning-based scoring

---

## Project Status
Completed up to experience-based scoring.
Further enhancements planned.
