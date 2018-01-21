from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, request
from django.views.generic import TemplateView
from django.utils import timezone

from .models import Post
from .form import PostForm


def logout_user(request):
    """
    Remove the authenticated user's ID from the request and flush their session
    data.
    """
    logout(request)
    return redirect('login')

def login_user(request):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. 
    """
    user_au = authenticate(username=request.POST['username'], password=request.POST['password'])
    login(request, user_au)

class HomePageView(TemplateView):
    
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'sn/index.html', context={'posts': posts})
        else:
            return redirect('login')
 

class PostPageView(TemplateView):
    
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        return render(request, 'sn/post_detail.html', context={'post': post})

    def post(self, request, **kwargs):
        if 'Like' in request.POST:
            post_id = request.POST['Like']
            post = Post.objects.get(id=post_id)
            post.likes = post.likes + 1
            post.save() 
        else:
            post_id = request.POST['Unlike']
            post = Post.objects.get(id=post_id)
            post.unlikes = post.unlikes + 1
            post.save()           
        return redirect('home')
    

class PostNewView(TemplateView):
    
    def get(self, request, **kwargs):
        form = PostForm()
        return render(request, 'sn/post_edit.html', context={'form': form})

    def post(self, request, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        return redirect('home')


class AuthenticatedView(TemplateView):   
    
    def get(self, request, **kwargs): 
        login_form = AuthenticationForm()      
        return render(request, 'sn/login.html', context={'login_form': login_form})
   
    def post(self, request, **kwargs):
        login_form = AuthenticationForm(request.POST)
        try:
            login_user(request)
        except:
            return redirect('login')
        return redirect('home')


class RegisterView(TemplateView):    

    def get(self, request, **kwargs):
        register_form = UserCreationForm()     
        return render(request, 'sn/register.html', context={'register_form': register_form})
    
    def post(self, request, **kwargs):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            new_user.save()
            user_au = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user_au)               
            return redirect('home')
        return render(request, 'sn/register.html', context={'register_form': register_form})   

