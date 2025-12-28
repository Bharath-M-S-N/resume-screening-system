#This is main file for the entire project

import os
from preprocessing import clean_text
from vectorizer import vectorize_text
from similarity import cosine_sim
from pdf_reader import extract_text_from_pdf
from skills import extract_skills, calculate_final_score
from experience import extract_experience_years, experience_bonus


DATA_PATH = "../data"

def read_file(file_path):
    with open(file_path,"r", encoding="utf-8") as file:
        return file.read()
    
def load_resume(path):
    if path.endswith(".pdf"):
        return extract_text_from_pdf(path)
    else:
        return read_file(path)

#Main file to run the Resume Screening System

#Executes the complete resume screening pipeline
def main():

    #read job description
    job_path = os.path.join(DATA_PATH,"job_description.txt")
    job_text = read_file(job_path)
    clean_job = clean_text(job_text)

    resumes = []
    resume_names = []

    #read all resumes files
    for file in os.listdir(DATA_PATH):
        if file.startswith("resume"):
            full_path = os.path.join(DATA_PATH, file)
            raw_text = load_resume(full_path)
            cleaned_text = clean_text(raw_text)

            resumes.append(cleaned_text)
            resume_names.append(file)


    all_texts = resumes + [clean_job]

    tfidf_matrix = vectorize_text(all_texts)

    job_vector = tfidf_matrix[-1]

    results = []

    #similarity + skill scoring
    for i in range(len(resumes)):
        cosine_score = cosine_sim(tfidf_matrix[i], job_vector)

        skills_matched = extract_skills(resumes[i])

        # Experience extraction
        years = extract_experience_years(resumes[i])
        exp_bonus = experience_bonus(years)

        # Skill-based final score
        skill_score = calculate_final_score(cosine_score, skills_matched)

        # Total final score
        final_score = skill_score + exp_bonus

        results.append({
            "resume" : resume_names[i],
            "cosine_score": round(cosine_score, 3),
            "skills": skills_matched,
            "experience_years": years,
            "experience_bonus": exp_bonus,
            "final_score": round(final_score,3)
        })

    #Sort by final score
    results.sort(key=lambda x:x["final_score"], reverse=True)

    # Display results
    
    print("\nResume Ranking Based on Job Description\n")
    
    for rank, res in enumerate(results, start=1):
        print(f"Rank {rank} -> {res['resume']}")
        print(f"Cosine Score : {res['cosine_score']}")
        print(f"Skills Match: {res['skills']}")
        print(f"Final Score : {res['final_score']}")
        print(f" Experience : {res['experience_years']} years")
        print(f" Exp Bonus : {res['experience_bonus']}")
        print("-" * 40)

if __name__ == "__main__":
    main()
    






