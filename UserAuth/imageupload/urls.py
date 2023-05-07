from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload/', views.index, name="starting-page"),
    path('search/', views.search, name='search-page'),
    path('search/<slug:slug>/',views.image_detail, name='image-detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # path('thank-you/', views.thankyou)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
