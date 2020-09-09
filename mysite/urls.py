"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from mysite.views import IndexView

from bookmark.views import BookmarkLV, BookmarkDV
from blog.views import PostLV, PostDV

#   Static파일이란 웹 사이트 구성요소 중 Image, CSS, Script파일과 같이
#   그 내용이 고정되어 응답을 할 때 별도의 처리 없이 파일 내용을 그대로 보내주면 되는 파일을 의미합니다.
#   Static파일을 처리하기 위해서는 밑의 별도의 처리가 필요합니다.
from django.conf.urls.static import static # 밑의 (static)
from django.conf import settings # 별도의 (static)

urlpatterns = [
    ## url의 구조:
    #    "r'^" (기본) + 원하는주소
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^bookmark/$', BookmarkLV.as_view(), name='bookmark_index'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    url(r'^blog/$', PostLV.as_view(), name = 'blog_index'),
    url(r'^blog/(?P<pk>\d+)/$', PostDV.as_view(), name='blog_detail'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) # 처리 (static)
