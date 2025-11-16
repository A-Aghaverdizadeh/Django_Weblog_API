from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import Post, Category
from .serializer import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "status", "author"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination

    @action(["get"], detail=False)
    def get_hello(self, request):
        return Response({"message": "Hello World!!!"})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
