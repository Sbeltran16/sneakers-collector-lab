from django.forms import ModelForm
from .models import Buyer

class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'value', 'bought', 'size']
