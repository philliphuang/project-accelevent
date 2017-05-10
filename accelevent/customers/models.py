from django.db import models
from django.contrib.auth.models import User
from vendors.models import Vendor
from django.contrib.sessions.models import Session

class Customer(models.Model):
    # associates with built-in Django user
    user = models.OneToOneField(User, null=True, blank=True)
    
    # a user's cart of vendors
    cart = models.ManyToManyField(Vendor, blank=True)
    
    # tracks sessions with cookies
    session = models.ForeignKey(Session, null=True, blank=True)
    
    def __str__(self):
        if self.user == None:
            return self.session.session_key
        else: 
            return self.user.username