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
    print('query received: ', user_query)
    if not user_query:
        return jsonify({"error": "Invalid input"}), 400
    context = "You are an assistant. Please answer questions helpfully."
    prompt = f"Context: {context}\n\nUser Query: {user_query}\n\nResponse:"
    response = llm(prompt, max_length=50, num_return_sequences=1, return_full_text=False)["generated_text"]
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
