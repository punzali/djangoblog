from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import PostForm, RegisterForm
from .models import Post, Category
from django.db import models


# =========================================================
# REGISTER VIEW
# =========================================================

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


# =========================================================
# POST LIST VIEW
# =========================================================

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        ).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


# =========================================================
# MY POSTS VIEW
# =========================================================

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/my_posts.html"
    context_object_name = "posts"
    paginate_by = 6
    login_url = "login"

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        ).order_by("-created_at")


# =========================================================
# POST DETAIL VIEW
# =========================================================

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(
                models.Q(status="published")
                | models.Q(author=self.request.user)
            ).distinct()

        return Post.objects.filter(status="published")


# =========================================================
# CREATE POST VIEW
# =========================================================

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.success(
            self.request,
            "Post published successfully!"
        )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"slug": self.object.slug}
        )


# =========================================================
# UPDATE POST VIEW
# =========================================================

class PostUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def test_func(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        messages.success(
            self.request,
            "Post updated successfully!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"slug": self.object.slug}
        )


# =========================================================
# DELETE POST VIEW
# =========================================================

class PostDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    login_url = "login"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        messages.success(
            self.request,
            "Post deleted successfully!"
        )
        return super().form_valid(form)


# =========================================================
# ABOUT PAGE
# =========================================================

def about(request):
    return render(
        request,
        "blog/about.html",
        {"team": "DjangoBlog Team"}
    )


# =========================================================
# CONTACT PAGE
# =========================================================

def contact(request):
    return render(request, "blog/contact.html")


# =========================================================
# CUSTOM 403 ERROR PAGE
# =========================================================

def custom_403(request, exception=None):
    return render(
        request,
        "blog/403.html",
        status=403
    )


def test_403(request):
    raise PermissionDenied