#List of expanded skills
SKILLS = ["python", "machine learning", "nlp","data analysis","tf-idf","cosine similarity","deep learning","pandas","numpy"]

def extract_skills(text):
    """ 
    Extracting matching skills from given text.
    Returns a list of matched skills.
    """
    text = text.lower()
    matched_skills = []

    for skill in SKILLS:
        if skill in text:
            matched_skills.append(skill)

    return matched_skills

def calculate_final_score(cosine_score, matched_skills):
    """ 
    Final score = cosine similarity + skill bonus.
    Each matched skill adds 0.05 bonus.
    """
    bonus = len(matched_skills) * 0.05
    final_score = cosine_score + bonus

    return final_score