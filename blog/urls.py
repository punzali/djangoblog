from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # Home / Post List
    # =========================

    path(
        "",
        views.PostListView.as_view(),
        name="home"
    ),


    # =========================
    # Static Pages
    # =========================

    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "contact/",
        views.contact,
        name="contact"
    ),


    # =========================
    # Create Post
    # =========================

    path(
        "post/new/",
        views.PostCreateView.as_view(),
        name="post_create"
    ),


    # =========================
    # Update Post
    # =========================

    path(
        "post/<slug:slug>/edit/",
        views.PostUpdateView.as_view(),
        name="post_update"
    ),


    # =========================
    # Delete Post
    # =========================

    path(
        "post/<slug:slug>/delete/",
        views.PostDeleteView.as_view(),
        name="post_delete"
    ),


    # =========================
    # Post Detail
    # =========================

    path(
        "post/<slug:slug>/",
        views.PostDetailView.as_view(),
        name="post_detail"
    ),
]