from django.shortcuts import render, redirect, get_object_or_404
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
        # Obtendo os parâmetros do POST
        parametro = request.POST.get('atualizar')
        retirada = request.POST.get('retirada')

        # Convertendo retirada para inteiro
        try:
            retirada = int(retirada)
        except ValueError:
            messages.add_message(request, constants.ERROR,
                                 'Quantidade de retirada inválida')
            return redirect(reverse('produtos'))

        # Obtendo a instância do produto
        produto = get_object_or_404(Produto, id=id)

        # Atualizando a situação
        produto.situacao = parametro

        # Realizando a subtração
        produto.aberto = produto.aberto - retirada

        # Salvando a instância atualizada no banco de dados
        produto.save()

        # Adicionando mensagem de sucesso
        messages.add_message(request, constants.SUCCESS,
                             'Produto atualizado com sucesso')

        return redirect(reverse('produtos'))

    else:
        # Lidar com outros métodos HTTP, se necessário
        messages.add_message(request, constants.ERROR,
                             'Método não permitido')
        return redirect(reverse('produtos'))
