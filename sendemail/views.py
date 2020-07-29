from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            
            subject = "Name: {}, Email: {}".format(subject,from_email)
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_DESTINATION],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return render(request, "email-success.html",{})
