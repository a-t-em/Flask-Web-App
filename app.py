from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

llm = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('./index.html')
  
@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query")
    context = "You are an assistant. Please answer questions helpfully."
    prompt = f"Context: {context}\n\nUser Query: {user_query}\n\nResponse:"
    response = llm(prompt, max_length=50, num_return_sequences=1, return_full_text=False)[0]["generated_text"]
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
