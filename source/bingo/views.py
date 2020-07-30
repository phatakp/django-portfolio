from django.shortcuts import render
from .models import Player
from django.views.generic import TemplateView, CreateView

# Create your views here.
class HomeView(CreateView):
    model = Player
    template_name = "bingo/index.html"
