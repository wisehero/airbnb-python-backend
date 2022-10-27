from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.Login.as_view()),
    path("log-out", views.Login.as_view()),
    path("token-login", obtain_auth_token),
    path("@<str:username>", views.PublicUser.as_view()),
]
