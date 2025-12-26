\# Resume Screening System



\## Problem Statement

Recruiters often receive a large number of resumes for a single job opening, making manual screening time-consuming and inefficient.

This process can delay hiring decisions and increase the chance of missing suitable candidates.

The Resume Screening System aims to automate the initial screening of resumes by comparing them with a given job description.

It analyzes textual content to measure relevance between resumes and job requirements.

The system provides similarity scores and ranks candidates to support faster and more accurate hiring decisions.



\## Inputs

\- Resume text

\- Job description text



\## Outputs

\- Similarity score for each resume

\- Ranked list of candidates



\## Initial Approach

The system will use TF-IDF to convert text into numerical features.

Cosine similarity will be applied to measure how closely resumes match the job description.



#### Section 1: Project Flow(Pine Line).



Resume Screening System – Workflow



First, the system takes the resume text of a candidate and the job description provided by the recruiter.

Then, both texts are cleaned by converting them to lowercase, removing unnecessary symbols, and eliminating common stop words.

After cleaning, the text data is converted into numerical form using the TF-IDF technique.

These numerical vectors are compared using cosine similarity to measure how closely the resume matches the job description.

A similarity score is generated for each resume.

Finally, resumes are ranked based on their scores, with higher scores indicating better matches.



#### Section 2: Concept Understanding.

### 

Term Frequency shows how often a word appears in a document.

If a skill appears many times in a resume, it means that skill is important for that candidate.


#### Inverse Document Frequency


Inverse Document Frequency reduces the importance of very common words.

Words that appear in almost every resume get lower weight, while rare but meaningful words get higher weight.

#### TF-IDF

TF-IDF gives high importance to words that are frequent in a specific resume but not common across all resumes.

This helps identify unique and relevant skills instead of common words.

#### Cosine similarity

Cosine similarity measures how similar two text documents are based on their direction.

A value close to 1 means the resume strongly matches the job description,

while a value close to 0 means they are very different.


#### Text Preprocessing

“Text preprocessing removes noise and standardizes text before vectorization.”


## Resume Ranking Output

The system calculates cosine similarity between each resume
and the job description using TF-IDF vectors.
Resumes are then ranked in descending order of similarity score.

## Features:

- PDF resume parsing
- Text preprocessing
- TF-IDF vectorization
- Cosine similarity ranking
- Skill-based score boosting

