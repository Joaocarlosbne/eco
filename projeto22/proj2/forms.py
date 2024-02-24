from django import forms
from .models import Produtos  
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos  
        fields = ['nome', 'preco', 'quantidade', 'descricao', 'slug', 'img_url', 'categoria']  

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Campo obrigatório. Informe um endereço de e-mail válido.',
    )

    data_de_nascimento = forms.DateField(
        help_text='Campo obrigatório. Informe sua data de nascimento. mm/dd/year',
    )

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['username', 'email', 'data_de_nascimento', 'password1', 'password2']