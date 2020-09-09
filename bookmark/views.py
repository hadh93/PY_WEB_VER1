from django.shortcuts import render
from django.views.generic import ListView, DetailView # 제네릭
from bookmark.models import Bookmark

# Create your views here.

class BookmarkLV(ListView): # 북마크 리스트뷰
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

