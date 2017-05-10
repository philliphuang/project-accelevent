from django.test import TestCase

class HomeTestCase(TestCase):
    
    # tests if pages loads successfully
    def test_homepage_loads(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)