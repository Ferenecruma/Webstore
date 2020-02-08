from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                send_mail(phone, message,phone, ['ferenecruma@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "detail.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')