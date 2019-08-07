from django.test import TestCase
from django.contrib.auth.models import User
from twitter.views import HomeView
from twitter.models import Tweet


class TestHomeView(TestCase):

    def test_get_method_returns_status_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_method_renders_appropriate_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "twitter/home.html")

    def test_tweet_list_on_home_page(self):
        user = User.objects.create_user(
            username="user1",
            password="password123"
        )
        tweet = Tweet.objects.create(
            content="Some content",
            user=user
        )

        response = self.client.get("/")

        self.assertIn(tweet.content, response.content.decode("utf-8"))
