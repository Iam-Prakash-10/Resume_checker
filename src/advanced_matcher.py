import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from src.embedding_model import get_embedding

def advanced_role_matching(resume_text):
    df = pd.read_csv("data/job_roles.csv")

    resume_embedding = get_embedding(resume_text)

    similarities = []
    for _, row in df.iterrows():
        role_embedding = get_embedding(row["skills"])
        score = cosine_similarity(
            [resume_embedding],
            [role_embedding]
        )[0][0]
        similarities.append(round(score * 100, 2))

    df["semantic_match"] = similarities
    return df.sort_values(by="semantic_match", ascending=False)
