import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "flask-hosting")))
from app import app  # Import your Flask app object from the main .py file

class BasicTests(unittest.TestCase):

    # Executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### Tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
