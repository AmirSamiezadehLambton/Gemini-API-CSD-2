import unittest
from gemini_api import generate_content
from dotenv import load_dotenv


class TestGeminiAPI(unittest.TestCase):
    # Load the environment variables in the setUp function
    # Since it's already defined in gemini_api.py, this function is not doing anything for us here
    def setUp(self):
        load_dotenv("../.env")

    def test_valid_prompt_1(self):
        # Test for a valid prompt within the topic
        prompt = "How do I deploy a Flask app with GitHub Actions?"
        response = generate_content(user_prompt=prompt)
        # print(response)
        # check if "Flask" is part of the response
        self.assertIn("Flask", response)
        # check if "GitHub" is part of the response
        self.assertIn("GitHub", response)

    def test_invalid_prompt_1(self):
        # Test for an invalid prompt within the topic
        prompt = "Tell me about quantum mechanics."
        response = generate_content(user_prompt=prompt)
        print(response)
        # check if generic response is part of the response
        self.assertIn("I can only answer questions about flask, GitHub CI/CD pipeline, and Docker container", response)


















