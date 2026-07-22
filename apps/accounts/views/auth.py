from django.shortcuts import render
from django.http import HttpResponse


def login_view(request):
    return render(request, "accounts/login.html")

def register_view(request):
    return render(request, "accounts/register.html")

def logout_view(request):
    return HttpResponse("Logout Page")