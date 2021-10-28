from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


class PostMenu(ListView):
    model = Menu
    template_name = 'shop/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Burger Bachelor Maxican'
        return context


class About(ListView):
    model = About
    template_name = 'shop/about.html'
    context_object_name = 'imag'


class Menu(ListView):
    model = Menu
    template_name = 'shop/Menu.html'
    context_object_name = 'posts'


class Panel(ListView):
    model = Panel
    context_object_name = 'menu'


def contact(request):
    return render(request, 'shop/contact.html')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "shop/index.html"


