from django.conf.urls import url
from . import views
from .views import VendorDetail, VendorUpdate, VendorSearch, VendorSignup, VendorList, VendorLogin


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)', VendorDetail.as_view(), name='vendor_detail'),
    url(r'^update/(?P<pk>[0-9]+)$', VendorUpdate.as_view(), name='vendor_update'),
    url(r'^signup/(?P<pk>[0-9]+)$', VendorSignup.as_view(), name='vendor_signup'),
    url(r'^search$', VendorSearch.as_view(), name='vendor_search'),
    url(r'^list$', VendorList.as_view(), name='vendor_list'),
    url(r'^login$', VendorLogin.as_view(), name='vendor_login'),
    
    # login URLs
    #url(r'^login$', views.login, name = 'login'),
    #url(r'^auth$', views.auth_view, name = 'auth'), 
    url(r'^logout$', views.logout, name = 'logout'), 
    #url(r'^invalid$', views.invalid_login, name = 'invalid_login'),
]
  