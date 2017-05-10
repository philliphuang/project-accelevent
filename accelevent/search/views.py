from customers.views import SessionMixin, GetCustomerMixin
from vendors.models import Vendor
from django.views.generic import TemplateView
import urllib, urllib2, json
from operator import attrgetter
# from itertools import chain  for use with combining querysets

class NearbySearchMixin(object):
    def get_nearby(self):
        query = self.request.GET.get('inputQuery')
        
        # changes a "None" query to blank to avoid searching "None"
        if query is None:
            query = ''
            
        # formats the Google API parameters into proper url format
        parameters = urllib.urlencode({
                # Javier's API Key, DO NOT USE IN PRODUCTION
                'key' : 'AIzaSyC_We1jl6Q1udk8QulJfeu1zinYOMNepm4',
                # Boston
                'location' : '42.3601,-71.0589',
                # arbitrary
                'radius' : '50000',
                # phrase searched
                'keyword' : query
        })
        
        # requests and parses JSON object from Google Places Nearby Search API
        request_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?%s" % parameters
        response = urllib2.urlopen(request_url).read()
        data = json.loads(response)
        result_list = []
        
        # Generates results in Vendor format from returned JSON
        for item in data["results"]:
            
            # grabs basic information from returned JSON
            name_temp = item["name"]
            place_id_temp = item["place_id"]
            price_level_temp = item.get("price_level")
            rating_temp = item.get("rating")
            
            # creates and updates Vendors if needed
            new_vendor = Vendor.objects.update_or_create(
                
                # searches for existing Vendors using name and place_id
                name=name_temp, 
                place_id=place_id_temp, 
                
                # adds price level and rating if not defined already
                defaults={'price_level' : price_level_temp, 'rating' : rating_temp}) 
            
            # adds results to the result list
            result_list.append(new_vendor[0]) 
        
        # orders vendors with additional info first, ordering beyond that is pretty random
        result_list.sort(key=attrgetter('additional_info'), reverse=True)
        return result_list


"""Displays search request results or all listings if no request along with shopping cart"""
class ResultView(SessionMixin, TemplateView, NearbySearchMixin, GetCustomerMixin):
    template_name = "search/results.html"
    
    # returns the results list and cart list to template
    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['cart_list'] = self.get_customer().cart.all()
        context['result_list'] = self.get_nearby()
        query = self.request.GET.get('inputQuery')
        context['inputQuery'] = query
        return context