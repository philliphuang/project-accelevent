from django.conf.urls import url
from . import views
from .views import AddCart, RemoveCart
# from .views import CustomerSignupView

urlpatterns = [
    url(r'^cart/(?P<pk>[0-9]+)/add/$', AddCart.as_view(), name="add_cart"),
    url(r'^cart/(?P<pk>[0-9]+)/remove/$', RemoveCart.as_view(), name="remove_cart"),
]