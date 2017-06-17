from django.contrib import admin
from app_estoque.models import *
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Retira_Produto)
admin.site.register(Compra_Produto)
