from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'CoreyMS', 
        'title': 'Blog Post 1', 
        'content': 'First post content', 
        'date_posted': 'January 10, 2021'
    }, 
    {
        'author': 'Lokesh Harad', 
        'title': 'Blog Post 2',
        'content': 'Second post content', 
        'date_posted': 'February 10, 2021'
    }
]


def home(request):
    
    context = {
        'posts': posts
    }
    # return HttpResponse("<h1>Blog Home</h1>")
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse("<h1>Blog About</h1>")
    return render(request, 'blog/about.html', {'title': 'About'})