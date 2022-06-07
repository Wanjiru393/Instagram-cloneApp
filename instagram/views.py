from django.shortcuts import render, redirect
from .models import Post, Stream, Tag
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
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


# @login_required()
def NewPost(request):
    user = request.user.id
    tags_objs = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("image")
            caption = form.cleaned_data.get("caption")
            tags_form = form.cleaned_data.get("tags")

            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)

            p, created = Post.objects.get_or_create(image=image, caption=caption, user_id=user)
            p.tags.set(tags_objs)
            p.save()
            return redirect('index')

    else:
        form = NewPostForm()

    context = {'form': form}

    return render(request, 'instagram/newpost.html', context)

