from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from twitter.models import Tweet


class HomeView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, "twitter/home.html", {
            "tweets": tweets
        })

    def post(self, request):
        content = request.POST.get("content")
        user = request.user

        Tweet.objects.create(
            content=content,
            user=user
        )
        # return self.get(request)
        return redirect("/")


class UserDetailView(View):
    def get(self, request, username):
        tweets = Tweet.objects.filter(user__username=username)
        return render(request, "twitter/user_detail.html", {
            "tweets": tweets
        })


class TweetDetailView(View):
    def get(self, request, pk):
        tweet = Tweet.objects.get(pk=pk)
        return render(request, "twitter/tweet_detail.html", {
            "tweet": tweet
        })
