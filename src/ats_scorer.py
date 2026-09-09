def calculate_ats_score(resume_skills, required_skills):
    resume_skills = set([s.lower() for s in resume_skills])
    required_skills = set([s.lower() for s in required_skills])

    if not required_skills:
        return 0, []

    matched = resume_skills.intersection(required_skills)

    # ----------------------------
    # Skill match ratio
    # ----------------------------
    skill_ratio = len(matched) / len(required_skills)

    # ----------------------------
    # Penalty: too few required skills
    # ----------------------------
    skill_penalty = min(len(required_skills) / 10, 1.0)

    # ----------------------------
    # Penalty: shallow resume
    # ----------------------------
    depth_penalty = min(len(resume_skills) / 15, 1.0)

    # ----------------------------
    # Final ATS Score
    # ----------------------------
    ats_score = (
        70 * skill_ratio +
        20 * skill_penalty +
        10 * depth_penalty
    )

    return round(ats_score, 2), list(matched)
