from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUserView, ProfileUpdateView, FollowUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),  # TokenAuth
    path("me/", ProfileUpdateView.as_view(), name="profile-update"),
    path("<int:user_id>/follow/", FollowUserView.as_view(), name="follow_user"),
]
