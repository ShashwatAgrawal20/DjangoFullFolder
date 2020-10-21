from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def about (request):
    return render(request, 'home/about.html')

def contact (request):
    # We are giving the values to the database
    if request.method=='POST':
        # For Example - making a variable and showing request.POST['name'] and giving the name which we have given in the contact.html this is so important don't mess with it
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # Making of contact and giving the main class and giving the aurgument given in it to store the values
        contact = Contact(name=name, email=email, phone=phone, content=content)
        # Finally saving the contact and we can see the contact form sucessfully in the database or adimin pannel
        contact.save()
    return render(request, 'home/contact.html')