from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from .views import PostView


urlpatterns = [
    path('upload/', views.index, name="starting-page"),
    path('search/', views.search, name='search-page'),
    path('search/<slug:slug>', views.image_detail, name = 'image-detail'),
    
    path('', views.logout_view, name='signout')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
