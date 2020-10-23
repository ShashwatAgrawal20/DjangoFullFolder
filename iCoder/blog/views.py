from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
    # Getting all the values of the Post in the allPosts variable
    allPosts = Post.objects.all()
    # Making a dictionary and giving it a name of context and giving it the key and pair of allPosts
    context = {'allPosts': allPosts}
    # Passing the dictionary to the blog/blog.html in templates
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)
