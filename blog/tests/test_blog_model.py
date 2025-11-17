from django.test import TestCase

# from datetime import datetime
from accounts.models.profile import Profile
from accounts.models.accounts import User
from ..models import Post


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="aghaverdi@gmail.com", password="Aa13311331@"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test first name",
            last_name="test last name",
            description="test content",
        )

    def test_post_model_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="test post",
            content="test description",
            status=True,
            category=None,
            published_date="2025-10-30T19:38:37Z",
        )
        self.assertEqual(post.title, "test post")
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
