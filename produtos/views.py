from django.shortcuts import render, redirect
from setup import urls
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from .models import Produto
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def produtos(request):
    if request.method == "GET":
        user = request.user
        nome = request.GET.get('nome')
        # filtra o que vc quer buscar, nesse caso os eventos do usuário logado
        produtos = Produto.objects.all().order_by('nome')
        if nome:
            produtos = produtos.filter(nome__contains=nome)
        return render(request, 'produtos.html', {'produtos': produtos, 'user': user})


@login_required
def atualiza(request, id):
    if request.method == "POST":
        parametro = request.POST.get('atualizar')
        produto = Produto.objects.filter(id=id)
        produto.update(situacao=parametro)
        messages.add_message(request, constants.SUCCESS,
                             'Produto atualizado com sucesso')

        return redirect(reverse('produtos'))
