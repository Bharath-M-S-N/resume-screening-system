# Main file to run the Resume Screening System

import os
from preprocessing import clean_text
from vectorizer import vectorize_text
from similarity import cosine_sim
from pdf_reader import extract_text_from_pdf
from skills import extract_skills, calculate_final_score
from experience import extract_experience_years, experience_bonus
import traceback

DATA_PATH = "../data"

def read_file(file_path):
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                raise ValueError("File is empty")
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {e}")
    
def load_resume(path):
    try:
        if path.endswith(".pdf"):
            text = extract_text_from_pdf(path)
        else:
            text = read_file(path)

        if not text.strip():
            raise ValueError("Resume content is empty")
        
        return text
    
    except Exception as e:
        print(f"⚠️ Skipping resume {os.path.basename(path)}:{e}")
        return None
    
# Display the results    
def print_results(results):
    print("\n" + "=" * 60)
    print("📄 RESUME SCREENING RESULTS")
    print("=" * 60)

    for rank, res in enumerate(results, start=1):
        print(f"\n🏆 Rank {rank}")
        print(f"Resume Name       : {res['resume']}")
        print(f"Cosine Similarity : {res['cosine_score']}")
        print(f"Skills Matched    : {', '.join(res['skills']) if res['skills'] else 'None'}")
        print(f"Experience        : {res['experience_years']} years")
        print(f"Experience Bonus  : {res['experience_bonus']}")
        print(f"Final Score       : {res['final_score']}")
        print("-" * 60)



#Executes the complete resume screening pipeline
def main():
    try:
        print("\n🚀 Resume Screening System Started\n")

        # Read job description
        job_path = os.path.join(DATA_PATH, "job_description.txt")
        job_text = read_file(job_path)

        if not job_text.strip():
            raise ValueError("Job desciption file is empty")
        
        clean_job = clean_text(job_text)

        resumes = []
        resume_names = []

        # Read resume File
        for file in os.listdir(DATA_PATH):
            if file.startswith("resume"):
                full_path = os.path.join(DATA_PATH, file)

                raw_text = load_resume(full_path) 
                if raw_text is None or not raw_text.strip():
                    print(f"⚠️ Skipping empty or invalid resume: {file}")
                    continue

                cleaned_text = clean_text(raw_text)

                resumes.append(cleaned_text)
                resume_names.append(file)


        if not resumes:
            raise ValueError("No valid resumes found in data folder.")
        
        #Vectorization
        all_texts = resumes + [clean_job]
        tfidf_matrix = vectorize_text(all_texts)
        job_vector = tfidf_matrix[-1]

        results = []


        for i in range(len(resumes)):
            cosine_score = cosine_sim(tfidf_matrix[i], job_vector)

            skills_matched = extract_skills(resumes[i])

            years = extract_experience_years(resumes[i])
            exp_bonus = experience_bonus(years)

            skill_score = calculate_final_score(cosine_score, skills_matched)

            final_score = skill_score + exp_bonus

            results.append({
                "resume": resume_names[i],
                "cosine_score": round(cosine_score, 3),
                "skills": skills_matched,
                "experience_years": years,
                "experience_bonus": exp_bonus,
                "final_score": round(final_score, 3)
            })

        # Sort by Final Score
        results.sort(key=lambda x: x["final_score"], reverse=True)

        print_results(results)
        top_candidate = results[0]

        print("\n✅ SUMMARY")
        print("=" * 60)
        print(f"Best Match Resume : {top_candidate['resume']}")
        print(f"Final Score      : {top_candidate['final_score']}")
        print(f"Matched Skills   : {', '.join(top_candidate['skills']) if top_candidate['skills'] else 'None'}")
        print(f"Experience       : {top_candidate['experience_years']} years")
        print("=" * 60)

    except FileNotFoundError as e:
        print(f"\n❌ File Error: {e}")

    except ValueError as e:
        print(f"\n⚠️ Data Issue: {e}")

    except Exception as e:
        print(f"\n🔥Unexpected Error: {e}")


if __name__ == "__main__":
    main()








