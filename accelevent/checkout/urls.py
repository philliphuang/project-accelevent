from django.conf.urls import url
from . import views
from checkout.views import CheckoutView

urlpatterns = [
    url(r'^$', CheckoutView.as_view(), name='checkout'),
]
