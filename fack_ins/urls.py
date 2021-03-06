"""fack_ins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from comment.views import CommentView
from likes_and_dislikes.views import PostlikesToggleView

from django.urls import path, include

# import this so that to host static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('admin/', admin.site.urls),
    path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace='accounts')),
    path('register/', include(('register.urls', 'register'), namespace='register')),
    path('<int:post_id>/', CommentView.as_view(), name='comment'),
    path('<int:post_id>/<slug:slug>/', PostlikesToggleView.as_view(), name='like-toggle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)