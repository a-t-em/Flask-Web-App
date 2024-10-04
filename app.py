from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

llm = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('./index.html')

@app.route("/query", methods=["POST"])
def query():
    try:
        user_query = request.json.get("query")
        if not user_query:
            app.logger.error("Invalid input: No query provided")
            return jsonify({"error": "Invalid input"}), 400
        context = "You are an assistant. Please answer questions helpfully."
        prompt = f"Context: {context}\n\nUser Query: {user_query}\n\nResponse:"
        response = llm(prompt, max_length=50, num_return_sequences=1, return_full_text=False)[0]["generated_text"]
        return jsonify({"response": response})
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/test', methods=["GET"])
def test():
    return "Server is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)