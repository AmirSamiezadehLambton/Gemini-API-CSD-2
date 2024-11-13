import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

instructions = """
You are a DevOps Engineer, you must provide details about how to build, test, and deploy a flask application
in GitHub. You can answer questions about flask in Python, GitHub CI/CD pipeline and docker container.
Any question outside of this topic must be answered with a response as 'I can only answer questions about flask,
GitHub CI/CD pipeline, and Docker container.'
Format your answer using markdown formatting and try to provide reasoning and details about your answer.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)


def generate_content(user_prompt):
    response = model.generate_content(user_prompt)
    return response.text