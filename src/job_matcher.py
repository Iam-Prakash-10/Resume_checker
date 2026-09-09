import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_job_roles():
    df = pd.read_csv("data/job_roles.csv")
    return df

def match_resume_to_roles(resume_text):
    df = load_job_roles()

    documents = df["skills"].tolist()
    documents.append(resume_text)

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    df["match_percentage"] = (similarity[0] * 100).round(2)

    return df.sort_values(by="match_percentage", ascending=False)
