from rest_framework import serializers
from blog.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    get_url = serializers.ReadOnlyField(source="get_api_url")
    absolute_api_url = serializers.SerializerMethodField(method_name="get_abs_api_url")

    class Meta:
        model = Post
        fields = ['id', 'image', 'author', 'title', 'content', 'snippet', 'status', 'get_url', 'absolute_api_url', 'category', 'published_date']

    def get_abs_api_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
