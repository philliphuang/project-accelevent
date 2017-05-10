from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .views import Customer
from vendors.views import Vendor

class SessionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user('test', 'test@test.com', '1234')
        self.client.login(username='test', password='1234')
        Customer.objects.create(user=User.objects.get(username='test'))
        Vendor.objects.create(name='test1')
        
    def test_add_cart(self):
        person = User.objects.get(username='test')
        cust = Customer.objects.get(user=person)
        item = Vendor.objects.get(name='test1')
            
    def test_remove_cart(self):
        1 == 1
         