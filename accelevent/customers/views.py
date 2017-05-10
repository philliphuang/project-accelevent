from django.shortcuts import get_object_or_404
from .models import Customer
from vendors.models import Vendor
from django.contrib.sessions.models import Session
from django.views.generic.base import RedirectView

""" Handles User sessions """
class SessionMixin(object):
    # TODO test if accepts cookies and ensure login updates session
    # creates new session id for new user
    def dispatch(self, request, *args, **kwargs):
        if not request.session.exists(request.session.session_key): 
            request.session.create()
        return super(SessionMixin, self).dispatch(request, *args, **kwargs)

""" Obtains a Customer's cart based on the user's session key """
class GetCustomerMixin(object): 
    # gets the session id and returns the customer's cart field
    def get_customer(self):
        sess = Session.objects.filter(session_key=self.request.session.session_key).first()
        customer = Customer.objects.get_or_create(session=sess)
        # customer is a tuple, first is the Customer object, second is if created
        return customer[0]

""" Adds given item to user's cart """
class AddCart(SessionMixin, RedirectView, GetCustomerMixin):
    pattern_name = "add_cart"
    
    # gives HTTP 302 response
    permanent=False
    
    # adds object to cart and redirects to previous page
    def get_redirect_url(self, *args, **kwargs):       
        # finds selected vendor object
        result = get_object_or_404(Vendor, pk=kwargs['pk'])
        self.get_customer().cart.add(result)
        
        # sets url parameter to redirect to previous page
        self.url = self.request.META['HTTP_REFERER']
        return super(AddCart, self).get_redirect_url(*args, **kwargs)
    

""" Removes given item from user's cart """
class RemoveCart(SessionMixin, RedirectView, GetCustomerMixin):
    pattern_name = "remove_cart"
    
    # gives HTTP 302 response
    permanent=False

    # removes object from cart and redirects to previous page
    def get_redirect_url(self, *args, **kwargs):
        # finds selected vendor object
        result = get_object_or_404(Vendor, pk=kwargs['pk'])
        self.get_customer().cart.remove(result)
        
        # sets url parameter to redirect to previous page
        self.url = self.request.META['HTTP_REFERER']
        return super(RemoveCart, self).get_redirect_url(*args, **kwargs)