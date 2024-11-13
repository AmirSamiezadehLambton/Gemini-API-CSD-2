import unittest
from main import app
from dotenv import load_dotenv


class TestRoute(unittest.TestCase):
    def setUp(self):
        load_dotenv("../.env")
        self.client = app.test_client()
        self.client.testing = True

    def test_chat_post(self):
        response = self.client.post("/chat", json={"prompt": "How do I set up Docker for Flask?"})
        self.assertEqual(response.status_code, 200)

    def test_chat_get(self):
        response = self.client.get("/chat")
        self.assertEqual(response.status_code, 405)