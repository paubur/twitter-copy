from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from twitter.views import HomeView
from twitter.models import Tweet
from django.urls import reverse_lazy


class TestHomeView(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()
        self.user = create_user("user1")

    def test_get_method_returns_status_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_method_renders_appropriate_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "twitter/home.html")

    def test_tweet_list_on_home_page(self):
        tweet = Tweet.objects.create(
            content="Some content",
            user=self.user
        )

        response = self.client.get("/")

        self.assertIn(tweet.content, response.content.decode("utf-8"))

    def test_redirect_after_creating_hit(self):
        request = init_request()
        request.user = self.user
        request.method = "POST"
        request.POST = {
            "content": "Some Content"
        }
        response = HomeView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse_lazy("home"))

    def test_creating_tweet(self):
        request = init_request()
        request.user = self.user
        request.method = "POST"
        request.POST = {
            "content": "Some Content"
        }
        response = HomeView.as_view()(request)

        self.assertEqual(Tweet.objects.count(), 1)


class TestUserDetailView(TestCase):

    def setUp(self):
        self.user = create_user("user1")

    def test_all_user_tweets_displayed(self):
        tweet1 = Tweet.objects.create(
            content="Some content",
            user=self.user
        )
        tweet2 = Tweet.objects.create(
            content="Other content",
            user=self.user
        )

        response = self.client.get("/{}/".format(self.user.username))
        content = response.content.decode("utf-8")

        self.assertIn(tweet1.content, content)
        self.assertIn(tweet2.content, content)


class TestTweetDetailView(TestCase):
    """Test suite for TweetDetailView"""

    def setUp(self):
        self.user = create_user("user1")

    def test_get_method_tweet_in_content(self):
        tweet = self.create_tweet(self.user)

        response = self.client.get("/tweet/{}/".format(tweet.pk))
        content = response.content.decode("utf-8")

        self.assertIn(tweet.content, content)
        self.assertEqual(response.status_code, 200)

    def create_tweet(self, user):
        return Tweet.objects.create(
            content="content",
            user=user,
        )


def init_request():
    """Create request object to work with in tests"""
    request_factory = RequestFactory()
    request = request_factory.get("/")
    return request


def create_user(username):
    return User.objects.create_user(
        username=username,
        password="password123"
    )
