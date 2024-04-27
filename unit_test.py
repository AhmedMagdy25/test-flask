import unittest
import uuid
from app import db_connect

class AppTest(unittest.TestCase):
    def test_db_connect(self):
        conn = db_connect()
        cursor = conn.cursor()
        self.assertIsNotNone(cursor.execute('SELECT * FROM users').fetchone())
        conn.close()

if __name__ == '__name__':
    unittest.main()