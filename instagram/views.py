from django.shortcuts import render
from .models import Post

# Create your views here.


# class PostView(ListView):

#     template_name = 'index.html'
#     queryset =Post.objects.all()
#     context_object_name = 'posts'

def index(request):
    posts = Post.objects.all()
    return render(request, 'instagram/index.html', {'posts': posts})


# def create(request):
#     posts = Post.objects.all()
#     from_class = PostForm
#     return render(request,'post_create.html')

#     def form_valid(self,form):
#         print(form.cleaned_data)

