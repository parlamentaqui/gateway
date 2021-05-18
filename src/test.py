import unittest
from app import app

class AppTests(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.context = self.app.test_request_context()
        self.context.push()
        self.client = self.app.test_client()

    def test_index_status(self):
        request = self.client.get('/')
        self.assertEqual(200 , request.status_code)

    def test_index(self):
        request = self.client.get('/')
        self.assertEqual('Parlamentaqui Gateway!!!' , request.data.decode())
        self.assertGreaterEqual(len(request.data.decode()),2)

    def test_fake_status(self):
        request = self.client.get('/not_exist')
        self.assertEqual(404 , request.status_code)

    def tearDown(self):
        self.context.pop()

if __name__=='__main__':
    unittest.main()
