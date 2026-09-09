import streamlit as st

# ===============================
# IMPORTS
# ===============================
from src.utils import save_uploaded_file
from src.resume_parser import extract_text_from_pdf, extract_skills
from src.job_matcher import match_resume_to_roles
from src.advanced_matcher import advanced_role_matching
from src.ats_scorer import calculate_ats_score
from src.recommender import recommend_skills
from data.skill_roadmap import ROLE_SKILL_ROADMAP

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ===============================
# HEADER
# ===============================
st.markdown(
    """
    <h1 style='text-align: center;'>AI Resume Analyzer</h1>
    <p style='text-align: center; color: gray;'>
    Machine Learning & NLP Based Career Intelligence System
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

# ===============================
# FILE UPLOADER
# ===============================
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF only)",
    type=["pdf"]
)

# ==========================================================
# MAIN LOGIC (ONLY RUNS AFTER FILE UPLOAD)
# ==========================================================
if uploaded_file:

    # ---------------------------
    # STEP 1: SAVE & READ RESUME
    # ---------------------------
    file_path = save_uploaded_file(uploaded_file)
    resume_text = extract_text_from_pdf(file_path)

    # ---------------------------
    # STEP 2: SKILL EXTRACTION
    # ---------------------------
    skills = extract_skills(resume_text)
    skills = [s.lower() for s in skills]

    # ---------------------------
    # STEP 3: BASIC JOB MATCHING
    # ---------------------------
    role_matches = match_resume_to_roles(resume_text)
    best_role = role_matches.iloc[0]

    # ---------------------------
    # STEP 4: ATS SCORE (FIXED)
    # ---------------------------
    required_skills = best_role["skills"].split()
    ats_score, matched_skills = calculate_ats_score(
        skills, required_skills
    )

    # ---------------------------
    # STEP 5: ADVANCED MATCHING
    # ---------------------------
    advanced_matches = advanced_role_matching(resume_text)
    best_adv = advanced_matches.iloc[0]

    # ---------------------------
    # STEP 6: SKILL ROADMAP (FIXED LOGIC)
    # ---------------------------
    role_name = best_role["role"]
    roadmap_skills = ROLE_SKILL_ROADMAP.get(role_name, [])

    missing_skills = list(
        set(roadmap_skills) - set(skills)
    )

    # ===============================
    # FRONTEND TABS
    # ===============================
    tab1, tab2, tab3 = st.tabs(
        ["📄 Resume Analysis", "🎯 Job Matching", "🚀 Advanced AI"]
    )

    # ==================================================
    # TAB 1: RESUME + SKILLS
    # ==================================================
    with tab1:
        st.subheader("Resume Preview")
        st.text(resume_text[:900])

        st.subheader("Detected Skills")
        if skills:
            st.write(skills)
        else:
            st.warning("No skills detected.")

    # ==================================================
    # TAB 2: BASIC MATCHING + ATS + LEARNING
    # ==================================================
    with tab2:
        st.subheader("Job Role Matching (Basic ML)")
        st.dataframe(role_matches, width="stretch")

        st.markdown("### Best Match Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("Best Role", best_role["role"])
        col2.metric("Match %", f"{best_role['match_percentage']}%")
        col3.metric("ATS Score", f"{ats_score}%")

        st.subheader("Matched Skills")
        st.write(matched_skills)

        st.subheader("Missing Skills (Learning Roadmap)")
        if missing_skills:
            st.write(missing_skills)
        else:
            st.success("Your resume already matches the roadmap well.")

        st.subheader("Learning Recommendations")
        recommendations = recommend_skills(missing_skills)

        for rec in recommendations:
            st.write(
                f"• {rec['skill']} | Level: {rec['level']} | {rec['link']}"
            )

    # ==================================================
    # TAB 3: ADVANCED AI (BERT)
    # ==================================================
    with tab3:
        st.subheader("Advanced Semantic Matching (BERT)")
        st.markdown(
            "Transformer-based semantic matching using Sentence-BERT."
        )

        st.dataframe(
            advanced_matches[["role", "semantic_match"]],
            width="stretch"
        )

        st.success(
            f"Best AI Match: {best_adv['role']} "
            f"({best_adv['semantic_match']}%)"
        )

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption(
    "Built with Python, Machine Learning, NLP & Streamlit | Final Year Project"
)

