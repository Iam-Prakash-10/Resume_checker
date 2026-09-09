from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jobs(resume_vec, job_vecs):
    similarities = cosine_similarity(resume_vec, job_vecs)
    return similarities[0]
