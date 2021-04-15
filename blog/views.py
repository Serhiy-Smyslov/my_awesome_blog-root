from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def showblog(request):
    blogs = Blog.objects
    return render(request, 'blogs/blog.html', {'blogs': blogs})


def specific_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/specific_post.html',
                  {'post': blog})
