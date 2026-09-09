def weighted_skill_score(resume_skills, required_skills, weights):
    score = 0
    for skill, weight in zip(required_skills, weights):
        if skill in resume_skills:
            score += weight * 100
    return round(score, 2)
