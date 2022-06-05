from django.shortcuts import render
from .models import Post


# Create your views here.


# class PostView(ListView):

#     template_name = 'index.html'
#     queryset =Post.objects.all()
#     context_object_name = 'posts'

def index(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'index.html', context)

