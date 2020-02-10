from django.contrib import admin

from .models import Pic, Post, Comment

# Register your models here.

admin.site.register(Pic)
admin.site.register(Post)
admin.site.register(Comment)