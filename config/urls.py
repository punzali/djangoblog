
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

import debug_toolbar


urlpatterns = [
    path("admin/", admin.site.urls),

    # Login
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),

    # Logout
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),

    # Password reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="blog/password_reset.html",
            success_url="/password-reset/done/",
        ),
        name="password_reset",
    ),

    # Password reset email sent
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="blog/password_reset_done.html",
        ),
        name="password_reset_done",
    ),

    # Enter new password
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="blog/password_reset_confirm.html",
            success_url="/reset/done/",
        ),
        name="password_reset_confirm",
    ),

    # Password reset complete
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="blog/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),

    # Debug toolbar
    path("__debug__/", include(debug_toolbar.urls)),

    # Blog URLs
    path("", include("blog.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


handler403 = "blog.views.custom_403"
