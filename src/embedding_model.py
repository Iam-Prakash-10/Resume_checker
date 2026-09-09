from sentence_transformers import SentenceTransformer

# Lightweight but powerful model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return model.encode(text)
