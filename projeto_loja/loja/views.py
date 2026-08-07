from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


# Página inicial
def inicio(request):
    return render(request, "loja/inicio.html")


# READ - Listar produtos
def lista_produtos(request):
    produtos = Produto.objects.all()

    return render(
        request,
        "loja/lista_produtos.html",
        {"produtos": produtos}
    )


# CREATE - Criar produto
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista_produtos")

    else:
        form = ProdutoForm()

    return render(
        request,
        "loja/form_produto.html",
        {"form": form}
    )


# UPDATE - Editar produto
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(
            request.POST,
            instance=produto
        )

        if form.is_valid():
            form.save()
            return redirect("lista_produtos")

    else:
        form = ProdutoForm(instance=produto)

    return render(
        request,
        "loja/form_produto.html",
        {"form": form}
    )


# DELETE - Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.delete()
        return redirect("lista_produtos")

    return render(
        request,
        "loja/excluir_produto.html",
        {"produto": produto}
    )