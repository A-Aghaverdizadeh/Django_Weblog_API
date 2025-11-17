from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import BlogView, PostListView, PostDetailView


class TestUrl(SimpleTestCase):

    def test_blog_view_url_resolve(self):
        url = reverse("blog:blog")
        self.assertEqual(resolve(url).func.view_class, BlogView)

    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post_list")
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post_detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)
