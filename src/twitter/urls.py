from django.urls import path

from twitter.views import HomeView, UserDetailView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("<str:username>/", UserDetailView.as_view(), name="user_detail")
]
