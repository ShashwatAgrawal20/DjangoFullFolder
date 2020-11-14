from django.shortcuts import render

# Create your views here.

def blogHome(request):
    return render(request, 'blog/bloghome.html')
