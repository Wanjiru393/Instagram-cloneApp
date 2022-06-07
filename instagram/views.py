from django.shortcuts import render
from .models import Post,Stream
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.




# @login_required()
def index(request):
    user = request.user
    # posts = Post.objects.all()
    posts = Stream.objects.filter()

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-created_date')

    context = {
        'post_items': post_items,
    }
    return render(request, 'instagram/index.html', context )





