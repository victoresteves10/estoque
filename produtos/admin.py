from django.contrib import admin
from .models import Produto


@admin.register(Produto)
# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (

        "numero", "nome", "local",
        "descricao", "validade", "marca", "armazenamento", "situacao",
    )

    list_filter = ('situacao',)
    search_fields = ('produto',)
    list_per_page = 20

