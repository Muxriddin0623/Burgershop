from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')


def profile(request):
    return render(request, 'shop/index.html')

