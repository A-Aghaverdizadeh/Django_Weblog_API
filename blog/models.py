from django.db import models
from django.urls import reverse

# User = get_user_model()


class Post(models.Model):
    """
    weblog post model
    """

    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(
        "accounts.profile", on_delete=models.CASCADE, related_name="author"
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:25] + "...."

    def get_api_url(self):
        return reverse("blog:api-blog:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
