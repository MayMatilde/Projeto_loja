from django.shortcuts import render, redirect
from .forms import CriarUsuarioForm

def cadastro(request):
    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = CriarUsuarioForm()

    return render(request, 'cadastro.html', {'form': form})