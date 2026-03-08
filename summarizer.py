from transformers import pipeline

fast_model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
accurate_model = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text, mode):

    if mode == "fast":
        model = fast_model
        max_len = 100

    elif mode == "accurate":
        model = accurate_model
        max_len = 130

    else:
        model = accurate_model
        max_len = 200

    result = model(text, max_length=max_len, min_length=40, do_sample=False)

    return result[0]["summary_text"]