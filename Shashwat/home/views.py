from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
        # We are giving the values to the database
    if request.method=='POST':
        # For Example - making a variable and showing request.POST['name'] and giving the name which we have given in the contact.html this is so important don't mess with it
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your submission is recorded sucessfully")
    return render(request, 'home/contact.html')
