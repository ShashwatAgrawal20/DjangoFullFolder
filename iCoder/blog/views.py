from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

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
    comments = BlogComment.objects.filter(post=post)
    # print(request.user)
    context = {'post':post, 'comments':comments, 'user':request.user,}
    return render(request, 'blog/blogPost.html', context)


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(request, "Your comment has been posted successfully")
            comment.save()

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            messages.success(request, "Your reply has been posted successfully")
            comment.save()
        

    return redirect(f"/blog/{post.slug}")