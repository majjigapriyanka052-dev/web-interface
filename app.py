from flask import Flask, request, render_template
from google import genai

app = Flask(__name__)

client = genai.Client(api_key="your_API_key")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    action = request.form['action']

    if action == "answer":
        prompt = question
    elif action == "explain":
        prompt = f"Explain this topic in simple words: {question}"
    elif action == "summarize":
        prompt = f"Summarize the following text: {question}"
    elif action == "quiz":
        prompt = f"Generate a 5-question quiz on: {question}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return render_template(
    "result.html",
    question=question,
    answer=response.text
)
if __name__ == '__main__':
    app.run(debug=True)