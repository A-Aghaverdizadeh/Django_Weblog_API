from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-blog'

router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')

urlpatterns = router.urls

# urlpatterns = [
#     # path('post-list', views.PostList.as_view(), name='api_post_list'),
#     # path('post-detail/<int:pk>/', views.PostDetail.as_view(), name='api_post_detail'),
#     path('post-list', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
#     path('post-detail/<int:pk>', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
# ]   
