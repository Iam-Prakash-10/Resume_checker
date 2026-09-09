from sklearn.feature_extraction.text import TfidfVectorizer

def get_tfidf_features(resume_texts):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=500
    )
    features = vectorizer.fit_transform(resume_texts)
    return features, vectorizer
