from unittest import TestCase

from fastapi.testclient import TestClient

from ..application.main import app


class ApplicationTest(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_suggestions(self):
        response = self.client.get("/suggestions?q=Lon")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"suggestions": []})

    def test_get_suggestions__fail(self):
        response = self.client.get("/suggestions?q=")
        self.assertEqual(response.status_code, 422)
        self.assertEqual(list(response.json().keys()), ["detail"])
