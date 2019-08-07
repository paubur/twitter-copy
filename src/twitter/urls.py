from django.urls import path

from twitter.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='home')
]