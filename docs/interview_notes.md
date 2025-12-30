# Resume Screening System – Interview Notes

## 1. What problem does this project solve?
This project automates the initial resume screening process for recruiters.
Manual resume screening is time-consuming and inefficient when hundreds of resumes are received.
The system compares resumes with a job description using NLP techniques.
It ranks candidates based on relevance, skills, and experience.
This helps recruiters make faster and more accurate shortlisting decisions.

---

## 2. Why did you use TF-IDF instead of Word2Vec or embeddings?
TF-IDF is simple, interpretable, and effective for document similarity tasks.
It works well when labeled training data is not available.
TF-IDF highlights important words that are frequent in a resume but rare across all resumes.
Word embeddings require larger datasets and more computation.
For an initial screening system, TF-IDF is sufficient and efficient.

---

## 3. Why cosine similarity?
Cosine similarity measures the angle between two vectors rather than their magnitude.
This makes it ideal for comparing text documents of different lengths.
It focuses on content similarity instead of raw word count.
A higher cosine value means the resume closely matches the job description.
It is widely used in information retrieval systems.

---

## 4. How does your resume screening pipeline work?
First, resume and job description texts are collected.
The text is cleaned by lowercasing and removing noise.
TF-IDF converts the text into numerical vectors.
Cosine similarity calculates similarity scores.
Additional scoring is applied based on matched skills and experience.
Finally, resumes are ranked based on the final score.

---

## 5. How did you handle errors in the project?
I added error handling for missing files and empty resumes.
The system safely skips invalid or unreadable resumes.
Try-except blocks prevent the program from crashing.
Clear error messages are shown to the user.
This makes the system robust and production-ready.

---

## 6. How does skill-based scoring work?
A predefined list of skills is maintained.
The system checks which skills appear in the resume text.
Each matched skill contributes to a score boost.
This ensures that resumes with relevant technical skills rank higher.
Skill scoring improves accuracy beyond pure text similarity.

---

## 7. How does experience-based scoring work?
Regular expressions are used to extract experience information from resumes.
The system detects years of experience mentioned in the text.
Based on experience ranges, a bonus score is applied.
This helps prioritize candidates with more relevant experience.
It mimics real-world recruiter decision-making.

---

## 8. What challenges did you face while building this project?
Handling unstructured resume text was challenging.
Extracting experience reliably required careful regex design.
Balancing similarity score with skill and experience scores was important.
Ensuring the system does not crash on bad input was also a challenge.
These challenges improved my understanding of real-world NLP systems.

---

## 9. What did you learn from this project?
I learned how NLP is applied in real recruitment systems.
I gained hands-on experience with TF-IDF and cosine similarity.
I understood the importance of modular code design.
I learned how to handle edge cases and errors properly.
This project strengthened both my coding and problem-solving skills.

---

## 10. How can this project be improved in the future?
A web interface can be built using Streamlit.
Machine learning models can replace rule-based scoring.
Multiple job descriptions can be supported.
Database integration can be added for large-scale use.
Advanced NLP embeddings can improve accuracy further.


---

## 11. Project Status
Current version supports resume ranking using text similarity, skills, and experience.
The system is modular and GitHub-ready.
Future work includes UI integration and deployment as a web application.
