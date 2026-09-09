def ats_score(skills_found, required_skills):
    matched = set(skills_found).intersection(set(required_skills))
    score = (len(matched) / len(required_skills)) * 100
    return round(score, 2)
