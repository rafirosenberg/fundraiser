from django.forms import ModelForm

from models import Pledge #, Donor

class PledgeForm(ModelForm):
    class Meta:
        model = Pledge
    
# class DonorForm(ModelForm):
#     class Meta:
#         model = Donor