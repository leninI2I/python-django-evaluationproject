from django.urls import path
from . import views

app_name = "login"   


urlpatterns = [
    #path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path("", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("homepage/", views.homepage, name= "homepage"),
]