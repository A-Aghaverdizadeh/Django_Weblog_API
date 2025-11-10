from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import action
from rest_framework import status, mixins, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from blog.models import Post, Category
from .serializer import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination

"""
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=True)
    if request.method == 'GET':
        serialized = PostSerializer(post)
        return Response(serialized.data)
    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        post.delete()
        return Response({'detail': 'the post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
"""

'''
class PostList(APIView):
    """
        a class based view for showing list of posts
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """ retriving get method """
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ retriving post method and creating post with givin data """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

'''class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        serialized = PostSerializer(post)
        return Response(serialized.data)
    
    def put(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response({"detail": f"post {pk} is deleted successfully"})'''

'''class PostList(ListCreateAPIView):
    """
        a class based view for showing list of posts
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class PostDetail(RetrieveUpdateDestroyAPIView):
    """
        a class based view for showing single post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
'''

'''class PostViewSet(viewsets.ViewSet):
    """
        the first view writen with viewset to do all of the http actions at ones
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def list(self, request):
        post = Post.objects.filter(status=True)
        serializer = self.serializer_class(post, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response({"detail": f"post {pk} is deleted successfully"})'''

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'author']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination

    @action(['get'], detail=False)
    def get_hello(self, request):
        return Response({'message': 'Hello World!!!'})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
