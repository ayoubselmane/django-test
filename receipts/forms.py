from django import forms
from .models import Receipt
 
# create a ModelForm
class ReceiptForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Receipt
        fields = ['store','items_list','purchase_date','amount']


