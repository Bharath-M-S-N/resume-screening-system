import re

def extract_experience_years(text):
    """
    Extract years if experience from resume text.
    Returns maximum years found(int). If none found, returns 0
    """
    text = text.lower()

    # regex patterns to capture experiences
    patterns = [
        r'(\d+)\s*\+?\s*years?',
        r'(\d+)\s*\+?\s*yrs?',
        r'(\d+)\s*year experience',
        r'(\d+)\s*years experience'
    ]

    years_found = []

    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            years_found.append(int(match))

    if years_found:
        return max(years_found)
    
    return 0

def experience_bonus(years):
    """
    Calculate bonus score based on years of experience.
    """
    if years >= 4:
        return 0.10
    elif years >= 2:
        return 0.05
    else:
        return 0.0