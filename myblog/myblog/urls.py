"""findmyself URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myblogapp import views as my_views
from django.contrib.staticfiles import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_views.index, name='index'),
    url(r'^reg/$', my_views.reg, name='registion'),
    url(r'^login/$', my_views.login, name='login'),
    url(r'^logout/$', my_views.logout, name='logout'),
    url(r'^user_index/$', my_views.user_index, name='user_index'),
    url(r'^blog/(\d+)/$', my_views.blog, name='blog'),
    url(r'^blog_detailed/(\d+)/$', my_views.blog_detailed, name='blog_detailed'),
    url(r'^change_info/$', my_views.change_info, name='change_info'),
    url(r'^static/(?P<path>.*)$', views.serve),

]

# urlpatterns += staticfiles_urlpatterns()
