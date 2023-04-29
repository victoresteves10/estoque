from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR,
                                 'Username ou senha inválidos')
            return redirect(reverse('index'))

        auth.login(request, user)
        return redirect('produtos/')


def admin(request):
    return redirect('admin')