from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User


# Create your models here.
class LikesAndDislikes(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    date            = models.DateTimeField(auto_now_add=True)
    like_type       = models.BooleanField()                                     # 0 -> like, 1 -> dislike

    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')
