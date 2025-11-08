from django.urls import path, include
from .views import BlogView, RedirectToFlexi, PostListView, PostDetailView, PostFormView, PostCreateView, PostEditView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post-list/', PostListView.as_view(), name='post-list'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('create-form', PostFormView.as_view(), name='create-post'),
    path('create', PostCreateView.as_view(), name='create'),
    path('post-edit/<int:pk>/', PostEditView.as_view(), name='edit-post'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('flexi', RedirectToFlexi.as_view(), name='go-to-flexi'),
    path('api/v1/', include('blog.api.blog.urls')),
]
