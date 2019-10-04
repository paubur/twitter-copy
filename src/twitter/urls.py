from django.urls import path
from twitter.views import (
    HomeView,
    UserDetailView,
    TweetDetailView,
    MessageListView,
    MessageFormView
)

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("<str:username>/", UserDetailView.as_view(), name="user_detail"),
    path("tweet/<int:pk>/", TweetDetailView.as_view(), name="tweet_detail"),
    path("<str:username>/messages/",
         MessageListView.as_view(), name="user_messages"),
    path("send-message/", MessageFormView.as_view(), name="send_message"),
]
