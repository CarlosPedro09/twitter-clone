from django.urls import path
from .views import FollowUserView

urlpatterns = [
    path("follow/", FollowUserView.as_view(), name="follow-user"),
]
