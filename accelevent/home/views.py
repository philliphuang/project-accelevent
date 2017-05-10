from django.shortcuts import render
from django.views.generic.base import TemplateView

"""Renders homepage"""
class HomeView(TemplateView):
    template_name = "home/home.html" 