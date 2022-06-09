from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
from instagram.models import Post, Follow, Stream

from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve

# Create your views here.

def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = Profile.objects.all()

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page')
    posts_paginator = Paginator.get_page(page_number)

    context = {
        'posts': posts_paginator,
        'profile': profile,
    }

    return render(request, 'users/profile.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)

            return redirect('index')
            # Redirect to a success page.
        
        else:
            messages.success(request, ("There was An Error Logging In,Try Again... "))
            return redirect('login')
            
            pass


    else:
        return render(request, 'authenticate/login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))

    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Successfully Registered!'))
            return redirect('index')

    else:
            form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html',{
        'form':form,
    })





# @login_required()
def follow(request, username, option):
    
	following = get_object_or_404(User, username=username)

	try:
		f, created = Follow.objects.get_or_create(follower=request.user, following=following)

		if int(option) == 0:
			f.delete()
			Stream.objects.filter(following=following, user=request.user).all().delete()
		else:
			 posts = Post.objects.all().filter(user=following)[:25]

			 with transaction.atomic():
			 	for post in posts:
			 		stream = Stream(post=post, user=request.user, date=post.created_date, following=following)
			 		stream.save()

		return HttpResponseRedirect(reverse('profile', args=[username]))
	except User.DoesNotExist:
		return HttpResponseRedirect(reverse('profile', args=[username]))


