# pip install -q -U google-generativeai
# pip install flask
# pip install python-dotenv

from flask import Flask, request
from gemini_api import generate_content
app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    user_data = request.json
    user_prompt = user_data["prompt"]
    print("request.json content is: ", user_prompt)
    response = generate_content(user_prompt=user_prompt)
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")