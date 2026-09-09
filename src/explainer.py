def explain_match(semantic_score, skill_overlap):
    if semantic_score > 75 and skill_overlap > 60:
        return "Strong fit: Skills and experience align well."
    elif semantic_score > 50:
        return "Moderate fit: Some skill gaps exist."
    else:
        return "Weak fit: Significant upskilling required."
