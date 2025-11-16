# from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-blog"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")

urlpatterns = router.urls
