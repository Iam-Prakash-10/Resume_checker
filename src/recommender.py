from data.learning_resources import LEARNING_RESOURCES

def recommend_skills(missing_skills):
    recommendations = []

    for skill in missing_skills:
        skill = skill.lower()

        if skill in LEARNING_RESOURCES:
            info = LEARNING_RESOURCES[skill]
            recommendations.append({
                "skill": skill,
                "level": info["level"],
                "link": info["link"]
            })
        else:
            recommendations.append({
                "skill": skill,
                "level": "Beginner",
                "link": "Search official documentation or YouTube"
            })

    return recommendations
