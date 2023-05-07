from django.urls import path, include

from .views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView, SearchView
from core import views

app_name = 'post'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like', views.like_post, name='like_post'),
    #path('search',views.search, name="search"),
    path('results/', SearchView.as_view(), name='search'),
]
