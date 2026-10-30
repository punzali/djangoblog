
from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    RegisterView,
    MyPostsView,
    about,
    contact,
    test_403,
    test_404,
    test_500,
)


urlpatterns = [
    # Home page
    path(
        "",
        PostListView.as_view(),
        name="home",
    ),

    # My posts
    path(
        "my-posts/",
        MyPostsView.as_view(),
        name="my_posts",
    ),

    # Register
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

    # Create post
    path(
        "posts/create/",
        PostCreateView.as_view(),
        name="post_create",
    ),

    # Post detail
    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post_detail",
    ),

    # Edit post
    path(
        "posts/<slug:slug>/edit/",
        PostUpdateView.as_view(),
        name="post_update",
    ),

    # Delete post
    path(
        "posts/<slug:slug>/delete/",
        PostDeleteView.as_view(),
        name="post_delete",
    ),

    # About page
    path(
        "about/",
        about,
        name="about",
    ),

    # Contact page
    path(
        "contact/",
        contact,
        name="contact",
    ),

    # Custom 403 error page test
    path(
        "test-403/",
        test_403,
        name="test_403",
    ),
    path(
        "test-404/",
        test_404,
        name="test_404",
    ),
    path(
        "test-500/",
        test_500,
        name="test_500",
    ),
]
