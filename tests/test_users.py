import unittest, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "flask-hosting")))
from app import app, db


class UsersTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    ###############
    #### tests ####
    ###############

    def register(self, username, email, password):
        return self.app.post('/register',
                            data=dict(username=username,
                                      email=email,
                                      password=password, 
                                      confirm_password=password),
                            follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('test', 'test@example.com', 'FlaskIsAwesome')
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_username_registration(self):
        # Test case 1: Invalid username length
        response = self.register('t', 'test@example.com', 'FlaskIsAwesome')
        self.assertIn(b'Field must be between 2 and 20 characters long.', response.data)

        # Test case 2: Another invalid username condition
        response = self.register('ThisUsernameIsWayTooLong', 'test@example.com', 'FlaskIsAwesome')
        self.assertIn(b'Field must be between 2 and 20 characters long.', response.data)

    def test_invalid_email_registration(self):
        # Test case 1: Invalid email address format
        response = self.register('test2', 'test@example', 'FlaskIsAwesome')
        self.assertIn(b'Invalid email address.', response.data)

        # Test case 2: Another invalid email address condition
        response = self.register('test2', 'test@example..com', 'FlaskIsAwesome')
        self.assertIn(b'Invalid email address.', response.data)



if __name__ == "__main__":
    unittest.main()