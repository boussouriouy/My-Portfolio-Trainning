from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blog(request):
    #this is how tolist all the items in the database
    #obj = Blog.objects.all() 
    
    #This is how to pick the current one like the 3 current one
    
    obj = Blog.objects.order_by('-date') #[:5] That means we don't limit
    
    
    context = {
        'blogs_items':obj
    }
    return render(request, 'blog.html', context)


def detail(request, blog_id):
    obj = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blogs':obj
    }
    return render(request, 'detail.html', context)