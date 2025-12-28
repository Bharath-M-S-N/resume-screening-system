import re
import string

#This file handles text before vetorization

STOPWORDS = {
     "a", "an", "the", "and", "or", "but", "if", "while", "with",
    "is", "are", "was", "were", "be", "been", "being",
    "to", "of", "in", "on", "for", "from", "by", "at", "as",
    "this", "that", "these", "those"
}

#cleans resume and job description before vectorization
def clean_text(text):
    """
    Cleans and normalizes raw text input.
    Removes unwanted characters, extra spaces, and formatting issues.
    """

    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    text = re.sub(r"\d+","",text)
    words = text.split()
    filtered_words = [word for word in words if word not in STOPWORDS]
    cleaned_text = " ".join(filtered_words)

    return cleaned_text

if __name__ == "__main__":
    sample_text = "I am a Software Engineer with 2 years of experience in python"
    print("Original Text:")
    print(sample_text)

    print("\nCleaned Text:")
    print(clean_text(sample_text))