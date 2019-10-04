from django.urls import path

from twitter.views import HomeView, UserDetailView, TweetDetailView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("<str:username>/", UserDetailView.as_view(), name="user_detail"),
    path("tweet/<int:pk>/", TweetDetailView.as_view(), name="tweet_detail"),
]
