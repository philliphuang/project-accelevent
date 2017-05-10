from django.test import TestCase

class CheckoutTestCase(TestCase):
    
    # tests if pages loads successfully
    def test_checkout_loads(self):
        resp = self.client.get('/checkout/')
        self.assertEqual(resp.status_code, 200)
    
    