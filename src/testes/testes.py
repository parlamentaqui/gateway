import unittest
import requests
import mock

class EndpointGETTestCase(unittest.TestCase):

    def setUp(self):
        self.client = mock.Mock(spec=requests)
        self.data = EndpointGETTestCase(self.client)

    def test_status_server(self):
        self.client.get.return_value = mock.Mock(status_code=200)

        response = self.data.index()

        self.assertEqual(200, response.status_code)

    def test_status_deputies(self):
        self.client.get.return_value = mock.Mock(status_code=200)

        response = self.data.deputies_home()

        self.assertEqual(200, response.status_code)
        
    def test_status_parties(self):
        self.client.get.return_value = mock.Mock(status_code=200)

        response = self.data.parties()

        self.assertEqual(200, response.status_code)
        
    def test_status_federative_unities(self):
        self.client.get.return_value = mock.Mock(status_code=200)

        response = self.data.federative_unities()

        self.assertEqual(200, response.status_code)
        