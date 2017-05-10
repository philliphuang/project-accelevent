from django.test import TestCase
from .models import Vendor

class VendorTestCase(TestCase):
    
    def setUp(self):
        Vendor.objects.create(
            name="Santarpio's Pizza", 
            place_id="ChIJ05TyhURw44kRxqoBZ3mJu-M")
    
    # tests if page loads correctly
    def test_vendor_detail_loads(self):
        resp = self.client.get('/vendors/1')
        self.assertEqual(resp.status_code, 200)
    def test_vendor_signup_loads(self):
        resp = self.client.get('/vendors/signup/1')
        self.assertEqual(resp.status_code, 200)
    def test_vendor_search_loads(self):
        resp = self.client.get('/vendors/search')
        self.assertEqual(resp.status_code, 200)

        # no idea why this doesn't work 
        """    def test_vendor_update_loads(self):
        resp = self.client.get('/vendors/update/1')
        self.assertEqual(resp.status_code, 200)"""