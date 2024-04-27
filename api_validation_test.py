import unittest
import uuid
from app import app, db_connect

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_get_users(self):
        res = self.app.get('/api/users')
        self.assertEqual(res.status_code, 200, "success response expected")
        print(res.get_json())

    def test_user_exist_success(self):
        res = self.app.post('/api/users/test_154e43fb-1461-4670-878a-0ff6c2f4353f')
        self.assertEqual(res.status_code, 200, "success response expected")
        print(res.get_json())

    def test_user_exist_faild(self):
        res = self.app.post('/api/users/username')
        self.assertEqual(res.status_code, 404, "success response expected")
        print(res.get_json())

if __name__ == '__name__':
    unittest.main()