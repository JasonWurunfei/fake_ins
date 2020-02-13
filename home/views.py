# Http related
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Form related
from django import forms
from .forms import PostForm
# Models and Database related 
from .models import Pic, Post
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
# Others
import datetime

# Create your views here.


def home(request):
    posts = Post.objects.all()
    post_type = ContentType.objects.get(
                            app_label='home', model='post'
            )
    return render(request, 'home/home.html', context={"posts": posts, "post_type_id": post_type.id})


def post(request):
    initial_data = {
        'user_id'   : request.user.id,
        'pub_date'  : datetime.datetime.now()
    }


    if request.method == "POST":

        form = PostForm(request.POST, request.FILES, initial=initial_data)
        form.fields['user_id'].widget   = forms.HiddenInput()
        form.fields['pub_date'].widget  = forms.HiddenInput()


        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(id=request.user.id)
            new_pic = Pic(user=user, photo=data['photo'])
            new_pic.save()
            new_post = Post(user=user,
                            pics=new_pic,
                            pub_date=data['pub_date'],
                            post_text=data['post_text'])
            new_post.save()
            return HttpResponseRedirect('/')

        else:
            print("not valid")

    else:
        form = PostForm(initial=initial_data)
        form.fields['user_id'].widget   = forms.HiddenInput()
        form.fields['pub_date'].widget  = forms.HiddenInput()

        


    return render(request, 'home/post.html', context={'form': form})
