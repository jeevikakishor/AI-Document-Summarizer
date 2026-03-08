from keybert import KeyBERT

kw_model = KeyBERT()

def generate_keypoints(text):

    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )

    keypoints = [kw[0] for kw in keywords]

    return keypoints