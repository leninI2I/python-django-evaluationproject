from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView
)
from django.urls import reverse_lazy

from .views import signup, log_in, log_out, profile, edit_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/<username>/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('users:password_change_done')),
        name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),
]
