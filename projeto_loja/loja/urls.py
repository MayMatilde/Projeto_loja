from django.urls import path
from .views import (
    inicio,
    lista_produtos,
    criar_produto,
    editar_produto,
    excluir_produto,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("produtos/", lista_produtos, name="lista_produtos"),
    path("produtos/novo/", criar_produto, name="criar_produto"),
    path("produtos/editar/<int:id>/", editar_produto, name="editar_produto"),
    path("produtos/excluir/<int:id>/", excluir_produto, name="excluir_produto"),
]