import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_health_endpoint(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'UP', response.data)

if __name__ == "__main__":
    unittest.main()
