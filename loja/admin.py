from django.contrib import admin
# Register your models here.
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('criado_em', 'alterado_em',)
    empty_value_display = 'Vazio'
    list_display = ('Categoria', 'criado_em', 'alterado_em',)
    search_fields = ('Categoria',)

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('criado_em', 'alterado_em',)
    empty_value_display = 'Vazio'
    list_display = ('Fabricante', 'criado_em', 'alterado_em',)
    search_fields = ('Fabricante',)


class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria','fabricante', 'image',)
    def image_tag(self, obj):
        if obj.image:
            return '<img src="%s" width="100" height="100"/>' % obj.image.url
        return "Sem imagem"
    search_fields = ('Produto',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'preco', 'categoria','fabricante',)
    exclude = ('msgPromocao',)





admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)


