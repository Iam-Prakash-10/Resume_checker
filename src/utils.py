def save_uploaded_file(uploaded_file, path="temp.pdf"):
    with open(path, "wb") as f:
        f.write(uploaded_file.read())
    return path
