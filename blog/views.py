# from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class BlogView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "amir"
        context["posts"] = Post.objects.all()
        return context


class RedirectToFlexi(RedirectView):
    """
    a redirect view to redirect user to flexiconvert.ir
    """

    url = "https://flexiconvert.ir"


class PostListView(ListView):
    """
    a class based view for rendering list of posts
    """

    model = Post
    # queryset = Post.objects.all()
    paginate_by = 5
    context_object_name = "posts"
    ordering = "-id"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(DetailView):
    """
    a class based view for showing post details
    """

    model = Post


class PostFormView(LoginRequiredMixin, FormView):
    """
    a class based form view for creating post and saving it in db
    """

    template_name = "blog/post_form.html"
    form_class = PostForm
    success_url = "/blog/post-list/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    a class based create view for creating post automatically
    """

    model = Post
    fields = [
        "image",
        "title",
        "content",
        "status",
        "category",
        "published_date",
    ]
    success_url = "/blog/post-list/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        "image",
        "title",
        "content",
        "status",
        "category",
        "published_date",
    ]
    success_url = "/blog/post-list/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post-list/"
