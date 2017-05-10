from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, FormView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from search.views import NearbySearchMixin
from .models import Vendor 
from .forms import VendorUpdateForm, VendorSignupForm, VendorLoginForm
import urllib, urllib2, json

#login imports
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


"""START of Login Stuff"""

class VendorLogin(FormView):
    template_name = 'vendors/vendor_login.html'
    form_class = VendorLoginForm
    success_url = '/'
    
    def form_valid(self, form):
        if form.is_valid():
            auth.login(self.request, form.get_user())
        return super(VendorLogin, self).form_valid(form)

"""
def login(request):
    c = {}
    
    # Takes care of security
    c.update(csrf(request))
    return render(request, 'vendors/login.html', c)
 
# Makes sure that the proper username and password are inputted    

def auth_view(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    
    #returns None if the username and password do not match
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return render(request, 'home/home.html',{})
    else:
        return HttpResponseRedirect('invalid')

def invalid_login(request):
    return render_to_response('vendors/invalid_login.html')
"""

def logout(request):
    auth.logout(request)
    return render(request, 'home/home.html', {})
"""END of Login Stuff"""

""" List of vendors associated with account """
class VendorList(TemplateView):
    template_name = "vendors/vendor_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(VendorList, self).get_context_data(**kwargs)
        context['vendor_list'] = Vendor.objects.filter(
            login = self.request.user
        )
        return context

""" Allows vendor to be updated """
# TODO add template tags
class VendorUpdate(UpdateView):
    template_name = "vendors/vendor_update.html"
    model = Vendor
    form_class = VendorUpdateForm


""" Searches for and displays list of matching vendors through Google"""
class VendorSearch(TemplateView, NearbySearchMixin):
    template_name = "vendors/vendor_search.html"
    
    # returns vendor search results to the template
    def get_context_data(self, **kwargs):
        context = super(VendorSearch, self).get_context_data(**kwargs)
        context['result_list'] = self.get_nearby()
        context['inputQuery'] = self.request.GET.get('inputQuery')
        return context

""" Vendor account creation page after finding their Google listing"""
class VendorSignup(CreateView):
    template_name = "vendors/vendor_signup.html"
    form_class = VendorSignupForm
    success_url = '/'

    # Creates new User model and links it with a Vendor's login field
    def form_valid(self, form):
        # obtains correct Vendor
        vendor = Vendor.objects.get(pk=self.kwargs['pk'])
        
        user = form.instance
        
        # Hashes user-inputted password
        user.set_password(user.password)
        user.save()
        if vendor.login is None:
            # saves user account entry as account associated with the Vendor
            vendor.login = form.instance
        else:
            # prevents duplicate accounts from being associated with a Vendor
            raise Exception('User already exists') # make this more aesthetic
        vendor.save()
        return super(VendorSignup, self).form_valid(form)
    
""" Loads additional details about a Google search result """
class VendorDetail(DetailView):
    model = Vendor
    template_name = "vendors/vendor_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(VendorDetail, self).get_context_data(**kwargs)
        result = self.object
        
        # formats the Google API parameters into proper url format
        parameters = urllib.urlencode({
                # Javier's API Key, DO NOT USE IN PRODUCTION
                'key' : 'AIzaSyC_We1jl6Q1udk8QulJfeu1zinYOMNepm4',
                # place_id is Google's unique location identifier
                'placeid' : result.place_id
        })

        # requests and parses JSON object from Google Places Detail Search API
        request_url = "https://maps.googleapis.com/maps/api/place/details/json?%s" % parameters
        print request_url
        response = urllib2.urlopen(request_url).read()
        data = json.loads(response)
        obj = data['result']
        
        # grabs basic information from returned JSON
        context['name'] = obj.get('name')
        context['icon'] = obj.get('icon')
        context['address'] = obj.get('formatted_address')
        context['phone'] = obj.get('formatted_phone_number')
        context['website'] = obj.get('website')
        opening_hours = obj.get('opening_hours')
        if opening_hours:
            context['open_now'] = opening_hours['open_now']
            context['weekday_text'] = opening_hours['weekday_text']
        context['price_level'] = obj.get('price_level')
        context['rating'] = obj.get('rating')
        
        # grabs review information
        context['review_list'] = []
        if obj.get('reviews') is not None:
            for review in obj.get('reviews'):
                context['review_list'].append({
                        'author' : review.get('author_name'),
                        'rating' : review.get('rating'),
                        'text' : review.get('text'),     
                })          
                
        # obtains photos URLs with Google Places Photos API
        photo_list = []
        if obj.get('photos') is not None:
            for photo in obj.get('photos'):
                parameters = urllib.urlencode({
                        'key' : 'AIzaSyC_We1jl6Q1udk8QulJfeu1zinYOMNepm4',
                        'photoreference' : photo['photo_reference'],
                        'maxheight' : 500
                    })
                photo_string = "https://maps.googleapis.com/maps/api/place/photo?%s" % parameters
                photo_list.append(photo_string)
        context['photos'] = photo_list
        return context
