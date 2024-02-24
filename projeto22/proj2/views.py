from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Usuario, Produtos
from .forms import CustomUserCreationForm
from .forms import ProdutoForm
from django.http import JsonResponse

def home(request):
    categoria = request.GET.get('categoria', '')  # Obter o parâmetro categoria da requisição GET
    busca = request.GET.get('busca')

    if categoria:
        produtos = Produtos.objects.filter(categoria=categoria)
    elif busca:
        produtos = Produtos.objects.filter(nome__icontains=busca)
    else:
        produtos = Produtos.objects.all()

    categorias = Produtos.objects.values_list('categoria', flat=True).distinct()
    return render(request, 'home.html', {'produtos': produtos, 'categorias': categorias, 'categoria_selecionada': categoria})


@login_required
def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'add_produto.html', {'form': form})

def edit_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'edit_produto.html', {'form': form})

def delete_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('home')
    return render(request, 'delete_produto.html', {'produto': produto})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = Usuario.objects.filter(username=username).first()
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def produto_detalhes(request, slug):
    produto = get_object_or_404(Produtos, slug=slug)
    return render(request, 'produto_detalhes.html', {'produto': produto})

def buscar_produtos(request):
    busca = request.GET.get('busca')
    categoria = request.GET.get('categoria')
    
    produtos = Produtos.objects.all()

    if categoria:
        produtos = produtos.filter(categoria=categoria)

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    produtos_data = []
    for produto in produtos:
        produtos_data.append({
            'nome': produto.nome,
            'preco': produto.preco,
            'img_url': produto.img_url,
            'slug': produto.slug
        })

    return JsonResponse(produtos_data, safe=False)