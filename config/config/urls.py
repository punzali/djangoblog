from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

import debug_toolbar


# =========================================================
# URL PATTERNS
# =========================================================

urlpatterns = [

    # ADMIN
    path(
        "admin/",
        admin.site.urls,
    ),

    # LOGIN
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="blog/login.html"
        ),
        name="login",
    ),

    # LOGOUT
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="home"
        ),
        name="logout",
    ),

    # PASSWORD RESET
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="blog/password_reset.html"
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="blog/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="blog/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="blog/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    # DEBUG TOOLBAR
    path(
        "__debug__/",
        include(debug_toolbar.urls),
    ),

    # BLOG
    path(
        "",
        include("blog.urls"),
    ),
]


# =========================================================
# MEDIA FILES
# =========================================================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


# =========================================================
# CUSTOM 403 ERROR HANDLER
# =========================================================

handler403 = "blog.views.custom_403"