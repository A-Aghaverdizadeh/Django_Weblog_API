from django.test import TestCase

# from datetime import datetime
from ..forms import PostForm
from ..models import Category
from accounts.models.profile import Profile


class TestForm(TestCase):

    def test_post_form_with_valid_data(self):
        # user_obj = Profile.objects.create(
        #     email='admin@gmail.com'
        # )
        category_obj = Category.objects.create(name="test")
        form = PostForm(
            data={
                # 'author': user_obj.pk,
                "title": "test title",
                "content": "test content",
                "status": True,
                "category": category_obj,
                "published_date": "2025-10-30T19:38:37Z",
            }
        )
        self.assertTrue(form.is_valid())

    def test_post_form_with_onvalid_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
