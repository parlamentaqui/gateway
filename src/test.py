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


class CamaraTests(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.context = self.app.test_request_context()
        self.context.push()
        self.client = self.app.test_client()

    def test_index_camara_status(self):
        request = self.client.get('/camara')
        self.assertEqual(200 , request.status_code)
        self.assertEqual('Camara' , request.data.decode())
    
    def test_index_deputies_status(self):
        request = self.client.get('/camara/deputies')
        self.assertEqual(200 , request.status_code)

    def test_index_home_status(self):
        request = self.client.get('/camara/home')
        self.assertEqual(200 , request.status_code)

    def test_index_profile_id_status(self):
        request = self.client.get('/camara/profile/3')
        self.assertEqual(200 , request.status_code)


    def test_index_parties_status(self):
        request = self.client.get('/camara/parties')
        self.assertEqual(200 , request.status_code)


    def test_index_federative_unities_status(self):
        request = self.client.get('/camara/federative_unities')
        self.assertEqual(200 , request.status_code)

    def test_index_expenses_status(self):
        request = self.client.get('/camara/expenses')
        self.assertEqual(200 , request.status_code)

    def test_index_expenses_id_status(self):
        request = self.client.get('/camara/expenses/3')
        self.assertEqual(200 , request.status_code)

    def test_index_get_votes_by_deputy_id_status(self):
        request = self.client.get('/camara/get_votes_by_deputy_id/3')
        self.assertEqual(200 , request.status_code)

    def test_index_get_proposition_by_id_status(self):
        request = self.client.get('/camara/get_proposition_by_id')
        self.assertEqual(200 , request.status_code)

    def tearDown(self):
        self.context.pop()


if __name__=='__main__':
    unittest.main()
