from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import PledgeForm #, DonorForm

def pledge(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PledgeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/pledge/') # Redirect after POST
    else:
        form = PledgeForm() # An unbound form

    return render(request, 'pledges/index.html', {
        'form': form,
    })

# def newDonor(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = DonorForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#             form.save()

#             return HttpResponseRedirect('/pledge/donor/') # Redirect after POST
#     else:
#         form = DonorForm() # An unbound form

    return render(request, 'pledges/newdonor.html', {
        'form': form,
    })