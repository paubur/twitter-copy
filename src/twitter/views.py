from django.shortcuts import render
from django.views import View
from twitter.models import Tweet
# Create your views here.


class HomeView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, "twitter/home.html", {
            "tweets": tweets
        })
