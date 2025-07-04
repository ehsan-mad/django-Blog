from django.contrib import admin
from django.urls import path
from .views import (
    user_register,
    post_list,
    post_detail,
    like_post,
    post_create,
    post_update,
    post_delete,
    LogoutView,
)
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", post_list, name="post_list"),
    path("register/", user_register, name="user_register"),
    path(
        "login/",
        LoginView.as_view(template_name="blog/user_login.html"),
        name="user_login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="user_logout",
    ),
    path("post/<int:id>/", post_detail, name="post_detail"),
    path("post/<int:id>/like/", like_post, name="like_post"),
    path("post/create/", post_create, name="post_create"),
    path("post/<int:id>/update/", post_update, name="post_update"),
    path("post/<int:id>/delete/", post_delete, name="post_delete"),
]
