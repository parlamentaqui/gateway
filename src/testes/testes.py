import unittest
import requests
import mock

class EndpointGETTestCase(unittest.TestCase):

   def setUp(self):
       self.client = mock.Mock(spec=requests)
       self.data = EndpointGETTestCase(self.client)





