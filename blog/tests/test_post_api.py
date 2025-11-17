import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from accounts.models import User

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email='test@gmail.com',
        password='Aa13311331@',
    )
    return user

@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-blog:post-list")
        request = api_client.get(url)
        assert request.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-blog:post-list")
        data = {
            "title": "This is the post with id 4",
            "content": "This is the post with id 4 that we edited using put request inside Postman",
            "status": True,
            "published_date": timezone.now(),
        }
        request = api_client.post(url, data=data)
        assert request.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-blog:post-list")
        data = {
            "title": "This is the post with id 4",
            "content": "This is the post with id 4 that we edited using put request inside Postman",
            "status": True,
            "published_date": timezone.now(),
        }
        user = common_user
        api_client.force_authenticate(user=user)
        request = api_client.post(url, data=data)
        assert request.status_code == 201

    def test_create_post_novalid_data_400_status(self, api_client, common_user):
        url = reverse("blog:api-blog:post-list")
        data = {
            "title": "This is the post with id 4",
            "content": "This is the post with id 4 that we edited using put request inside Postman",
        }
        user = common_user
        api_client.force_authenticate(user=user)
        request = api_client.post(url, data=data)
        assert request.status_code == 400
    
