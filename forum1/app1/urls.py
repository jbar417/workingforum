from django.urls import path
from . import views

urlpatterns = [
    path("formpage", views.functionview1.as_view()),
    path("formpage/submitted", views.functionsubmitted),
    path("formpage/posts", views.PostsView.as_view()),
    path("", views.homepage),
]
