from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Category
from .forms import PostForm


# =========================
# Post List View
# =========================

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        ).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()

        return context


# =========================
# Post Detail View
# =========================

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        )


# =========================
# About Page
# =========================

def about(request):
    return render(
        request,
        "blog/about.html",
        {
            "team": "DjangoBlog Team"
        }
    )


# =========================
# Contact Page
# =========================

def contact(request):
    return render(
        request,
        "blog/contact.html"
    )


# =========================
# Create Post
# =========================

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "slug": self.object.slug
            }
        )


# =========================
# Update Post
# =========================

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "slug": self.object.slug
            }
        )


# =========================
# Delete Post
# =========================

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("home")