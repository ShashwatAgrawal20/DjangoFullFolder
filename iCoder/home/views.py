from django.shortcuts import render, HttpResponse, redirect, Http404
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

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
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form Correctly")

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
        # Finally saving the contact and we can see the contact form sucessfully in the database or adimin pannel
            contact.save()
            messages.success(request, "Your submission has been recorded Sucessfully")
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']

    if len(query) > 80:
        allPosts = Post.objects.none()


    else:
    # allPosts = Post.objects.all()
    # Getting a search by title
        allpoststitle = Post.objects.filter(title__icontains=query)
        # search by content
        allpostscontent = Post.objects.filter(content__icontains=query)
        # search by author name
        allpostsauthor = Post.objects.filter(author__icontains=query)
        allPosts = allpoststitle.union(allpostscontent).union(allpostsauthor)

    if allPosts.count() == 0:
        messages.error(request, "Please refine your search")

    params = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', params)


def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Checks for erroneous inputs:
        # Means checking the user is filling the form prefectly or not or the things are right 

        # Checking for the length of the username
        if len(username) > 10:
            messages.error(request, "Username should contains less than 10 characters or alphanumeric")
            return redirect ('home')
        
        if not username.isalnum():
            messages.error(request, "User name should be only alphanumeric")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')
        # Creat the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been sucuessfully created")
        return redirect("home")
    else:
        return HttpResponse(status = 404)

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect ('home')

def handleLogout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

