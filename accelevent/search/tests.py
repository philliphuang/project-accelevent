from django.test import TestCase
from customers.models import Customer
from vendors.models import Vendor

class SearchTestCase(TestCase):
    
    # tests if pages loads successfully
    def test_search_loads(self):
        resp = self.client.get('/search/results')
        self.assertEqual(resp.status_code, 200)
        
    # currently pretty useless
    def test_search_results(self):
        vendor_1 = Vendor.objects.create(name="test_vendor1")
        vendor_2 = Vendor.objects.create(name="test_vendor2")
        resp = self.client.get('/search/results')
        self.assertTrue('result_list' in resp.context)
        #self.assertTrue(vendor_1 in resp.context['result_list'])
        #self.assertTrue(vendor_2 in resp.context['result_list'])
    '''
    def test_cart_in_results(self):
        vendor_1 = Vendor.objects.create(name="test_vendor1")
        vendor_2 = Vendor.objects.create(name="test_vendor2")
        resp = self.client.get('/')
        sess = self.client.session
        print "YOY OYO YOY"
        print sess
        user = Customer.objects.get(session=sess)
        user.cart.add(vendor_1)
        resp = self.client.get('/search/results')
        self.assertTrue('cart_list' in resp.context)
        self.assertTrue(vendor_1 in resp.context['cart_list'])
        #self.assertFalse(vendor_2 in resp.context['cart_list'])
    '''
    
        