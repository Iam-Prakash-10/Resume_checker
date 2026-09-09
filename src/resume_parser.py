import pdfplumber
import pandas as pd
import re

# Load skills list
skills_df = pd.read_csv("data/skills.csv")
SKILLS = [skill.lower() for skill in skills_df["skill"].tolist()]

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text.lower()

def extract_skills(text):
    found_skills = set()
    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)
    return list(found_skills)
