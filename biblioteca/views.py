from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Livro
from .forms import LivroForm, PreferenciasForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'biblioteca/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'biblioteca/login.html', {'error': 'Invalid username or password'})
    return render(request, 'biblioteca/login.html')

@login_required
def dashboard(request):
    livros = Livro.objects.filter(usuario=request.user).select_related('autor', 'categoria')
    contagem_livros = Livro.objects.filter(usuario=request.user).count()
    livros_por_categoria = Livro.objects.filter(usuario=request.user).values('categoria__nome').annotate(total=Count('categoria')).order_by('-total')
    
    context = {
        'livros': livros,
        'contagem_livros': contagem_livros,
        'livros_por_categoria': livros_por_categoria,
    }
    return render(request, 'biblioteca/dashboard.html', context)

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('dashboard')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/adicionar_livro.html', {'form': form})

@login_required
def personalizar(request):
    if request.method == 'POST':
        form = PreferenciasForm(request.POST)
        if form.is_valid():
            request.session['cor_fundo'] = form.cleaned_data['cor_fundo']
            return redirect('dashboard')
    else:
        form = PreferenciasForm()
    return render(request, 'biblioteca/personalizar.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
