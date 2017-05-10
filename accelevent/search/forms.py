from django import forms
from vendors.models import Vendor

# creates Form that takes name of Cart_Item (currently unused)
class SearchBox(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name')