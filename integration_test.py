import unittest
import uuid
from app import app, db_connect

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_register(self):
        username = f'test_{uuid.uuid4()}'
        password = 'pass123'
        res = self.app.post('/register', data={'username': username, 'password': password})
        self.assertEqual(res.status_code, 200, "success response expected")
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE name = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(user, "user was not added")
        self.assertEqual(user['name'], username)

if __name__ == '__name__':
    unittest.main()