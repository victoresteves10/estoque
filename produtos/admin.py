from django.contrib import admin
from django.contrib import messages
from .models import Produto


@admin.register(Produto)
# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "numero", "nome", "local",
        "descricao", "validade", "marca", "aberto", "fechado", "situacao",
    )
    list_filter = ('situacao',)
    search_fields = ('produto',)
    list_per_page = 20

    def changelist_view(self, request, extra_context=None):
        print("changelist_view foi chamado")
        if extra_context is None:
            extra_context = {}

        # Chama o changelist_view padrão
        response = super().changelist_view(request, extra_context=extra_context)

        # Verifica os produtos com situacao 'acabou'
        produtos_acabou = Produto.objects.filter(situacao='Acabou')

        if produtos_acabou.exists():
            # Adiciona uma mensagem de aviso
            messages.warning(request, 'Há produtos com situação "acabou".')

        return response
