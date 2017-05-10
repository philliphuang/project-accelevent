from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

"""creates model for each service able to be added to carts"""
class Vendor(models.Model):
    # Google Places Information
    name = models.CharField(max_length=200)
    place_id = models.CharField(max_length=200, null=True, blank=True)
    price_level = models.SmallIntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    
    # Custom info entered by vendor
    additional_info = models.CharField(max_length=5000, null=True, blank=True)
    
    # Associated user if account created
    login = models.OneToOneField(User, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('vendors:vendor_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name