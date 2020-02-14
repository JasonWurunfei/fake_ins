from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from django.http import HttpResponse

from .forms import CommentForm
from .models import Comment
from django.contrib.auth.models import User

import sys
sys.path.append('../')
from home.models import Post

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import datetime

# Create your views here.
class CommentView(FormView):

    template_name = "comment/comment.html"
    form_class = CommentForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        user = request.user
        if user.is_authenticated:

            return self.render_to_response(
                self.get_context_data(post_id = kwargs['post_id'], post=Post.objects.get(id=kwargs['post_id']))
            )
        else:
            return HttpResponseRedirect('/accounts/login/')


    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        user = User.objects.get(id=request.user.id)
        comment_date = datetime.datetime.now()
        post_type = ContentType.objects.get(app_label='home', model='post')
        form = self.get_form()

        if form.is_valid():
            data = form.cleaned_data
            comment = Comment(
                user=user,
                pub_date=comment_date,
                comment_text=data['comment_text'],
                content_type=post_type,
                object_id=kwargs['post_id'],
                )
            comment.save()
            self.success_url = '/{}'.format(int(kwargs['post_id']))
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

