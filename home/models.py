from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericRelation

import sys
sys.path.append('../')
from comment.models import Comment

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)


class Pic(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    photo           = models.ImageField(upload_to=user_directory_path)


class Post(models.Model):
    comments        = GenericRelation(Comment)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    pics            = models.ForeignKey(Pic, on_delete=models.CASCADE)
    pub_date        = models.DateTimeField('date published')
    post_text       = models.CharField(max_length=200)
    post_likes      = models.IntegerField(default=0)
    post_dislikes   = models.IntegerField(default=0)



    


