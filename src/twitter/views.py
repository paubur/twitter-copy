from django.shortcuts import render, redirect
from django.views import View
from twitter.models import Tweet
# Create your views here.
from django.http import HttpResponse


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
