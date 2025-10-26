from django.urls import path
from . import views

urlpatterns = [
    # Home / Feed
    path("", views.home, name="home"),

    # Posts
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    path("comment/<int:post_id>/", views.comment_post, name="comment_post"),
    path("share/<int:post_id>/", views.share_post, name="share_post"),

    # Autenticação
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
