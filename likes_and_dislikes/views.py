from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View

from .models import LikesAndDislikes
from django.contrib.contenttypes.models import ContentType

import datetime
# Create your views here.

class PostlikesToggleView(View):
    app_name = 'home'
    model_name = 'post'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            post_type = ContentType.objects.get(
                            app_label=self.app_name, model=self.model_name
            )
            post_id = kwargs['post_id']
            is_done = LikesAndDislikes.objects.filter(
                user_id=user.id,
                content_type=post_type.id,
                object_id=post_id
            )
            if is_done:
                print("done")
                like_type = is_done.get().like_type
                choices = {'like': True, 'dislike': False} 
                print(like_type)
                print(choices.get(kwargs['slug']))

                if like_type == choices.get(kwargs['slug']):
                    print("delete")
                    is_done.delete()
                else:
                    print("change")
                    obj = is_done.get()
                    obj.like_type = choices.get(kwargs['slug'])
                    obj.save()

            else:
                
                date = datetime.datetime.now()
                choices = {'like': True, 'dislike': False} 
                like_type = choices.get(kwargs['slug'])
                LikesAndDislikes.objects.create(
                    user=user,
                    date=date,
                    like_type=like_type,
                    content_type=post_type,
                    object_id=post_id
                )

            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('/accounts/login/')
        
