from customers.views import SessionMixin, GetCustomerMixin
from django.views.generic import TemplateView

""" Displays checkout page with cart items for a user """
class CheckoutView(SessionMixin, TemplateView, GetCustomerMixin):
    template_name = "checkout/checkout.html"

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context['cart_list'] = self.get_customer().cart.all()
        return context