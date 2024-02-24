from django.db import models
from django.contrib.auth.models import AbstractUser

class Produtos(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    quantidade = models.IntegerField() 
    descricao = models.CharField(max_length=200)  
    slug = models.SlugField(unique=True)
    img_url = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    data_de_nascimento = models.DateField()
    # Você pode adicionar outros campos conforme necessário

    # Defina related_names exclusivos para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',
        blank=True,
        help_text='Os grupos aos quais o usuário pertence.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',
        blank=True,
        help_text='Permissões específicas deste usuário.',
        verbose_name='permissões do usuário',
    )

    def __str__(self):
        return self.username