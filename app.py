from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the saved summarizer model
with open("summarizer_model.pkl", "rb") as f:
    summarizer = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    input_text = request.form["input_text"]
    summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
