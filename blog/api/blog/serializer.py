from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    get_url = serializers.ReadOnlyField(source="get_api_url")
    absolute_api_url = serializers.SerializerMethodField(method_name="get_abs_api_url")
    # category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Post
        fields = ['id', 'image', 'author', 'title', 'content', 'snippet', 'status', 'get_url', 'absolute_api_url', 'category', 'published_date']
        read_only_fields = ['author']

    def get_abs_api_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        rep['category'] = CategorySerializer(instance.category).data
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('get_url')
            rep.pop('absolute_api_url')
        else:
            rep.pop('content')
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
