import requests
from django.test import TestCase


# Create your tests here.

class AddressTest(TestCase):
    def test_query(self):
        r = requests.post('http://127.0.0.1:8000/address/query/',
                          data={
                              'name': 'tom'
                          })
        print(r.text)

    def test_add(self):
        pass

    def test_edit(self):
        pass

    def test_delete(self):
        pass
