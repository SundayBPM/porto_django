from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Blog

# Create your views here.
def home(request):
    """
    function to show home page
    """
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})

def warning(request):
    """
    This function used to show information to user that page they trying to access is restricted
    """
    return render(request, 'blog/warnings.html')
