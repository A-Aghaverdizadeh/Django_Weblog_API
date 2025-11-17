# from datetime import datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from accounts.models import User, Profile
from ..models import Post


class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="aghaverdi@gmail.com", password="Aa13311331@"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test first name",
            last_name="test last name",
            description="test content",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test post",
            content="test description",
            status=True,
            category=None,
            published_date=timezone.now(),
        )

    def test_blog_url_successfull_response(self):
        url = reverse("blog:blog")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("blog"))
        self.assertTemplateUsed(response, template_name="blog/index.html")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post_detail", kwargs={"pk": self.post.id})
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_anonymous_response(self):
        url = reverse("blog:post_detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
