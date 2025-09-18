from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from blog import models
from blog import forms



def index(request):
    posts = models.Post.objects.filter(published=True)
    return render(request, "blog/index.html", {
        "title": "All Posts",
        "posts": posts
    })


def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk, published=True)
    comments = post.comments.filter(published=True)

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.post = post
            form_obj.save()
            return redirect("blog:detail", pk=post.pk)
    else:
        form = forms.CommentForm()
    return render(request, "blog/detail.html", {
        "title": post.title,
        "post": post, 
        "form": form,
        "comments": comments
    })