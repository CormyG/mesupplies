from audioop import reverse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from bag import contexts

# Create your views here.

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		bag_items =contexts.bag_items
		if form.is_valid():
			subject = "Quaotation" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			'bag':bag_items
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'email', ['cormacgilbert@outlook.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('../')
      
	form = ContactForm()
	return render(request, "contact/contact.html", {'form':form})