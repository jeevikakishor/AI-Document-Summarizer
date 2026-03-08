from flask import Flask, render_template, request, jsonify
from summarizer import summarize
from keypoints import generate_keypoints
from pdf_utils import extract_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize_text():

    mode = request.form.get("mode")
    text = request.form.get("text")

    if "file" in request.files and request.files["file"].filename != "":
        file = request.files["file"]
        text = extract_text(file)

    summary = summarize(text, mode)

    keypoints = generate_keypoints(text)

    important_sentences = summary.split(". ")

    return jsonify({
        "summary": summary,
        "keypoints": keypoints,
        "sentences": important_sentences
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)