from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.live_update, name="live_update"),
    path("save/", views.save_snippet, name="save_snippet"),
    path("load/", views.load_snippet, name="load_snippet"),
]
