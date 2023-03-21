from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("delete", views.DeleteView.as_view()),
    path("delete_all", views.DeleteAllView.as_view())
]
