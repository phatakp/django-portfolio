from django.urls import path
from . import views

app_name = "bingo"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
]
