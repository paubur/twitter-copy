from django.test import TestCase
from twitter.views import HomeView


class TestHomeView(TestCase):

    def test_get_method_returns_status_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_method_renders_appropriate_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "twitter/home.html")
