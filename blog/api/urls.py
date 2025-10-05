from django.urls import path

from blog.api import views


urlpatterns = [
    path("tag/list/", views.TagListView.as_view()),
    path("tag/<int:pk>/", views.TagRetrieveView.as_view()),

    path("image/list/", views.PostImageListView.as_view()),
    path("image/<int:pk>/", views.PostImageRetrieveView.as_view()),

    path("comment/list/", views.CommentListCreateView.as_view()),
    path("comment/<int:pk>/", views.CommentRetrieveView.as_view()),

    path("post/list/", views.PostListView.as_view()),
    path("post/<int:pk>/", views.PostRetrieveView.as_view())
]