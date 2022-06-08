from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Stream, Tag, Likes
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from django.urls import reverse
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
def PostDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post': post,
    }

    return render(request, 'instagram/post_detail.html', context)




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



# @login_required()
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes

    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        like = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()
     
    return HttpResponseRedirect(reverse('postdetails', args=[post_id]))