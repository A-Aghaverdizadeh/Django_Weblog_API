from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status', 'category', 'created_date', 'published_date']
    list_filter = ['status', 'category', 'created_date', 'published_date']
    search_fields = ['author', 'title']

@admin.register(Category)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']