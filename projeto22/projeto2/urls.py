from django.contrib import admin
from django.urls import path
from proj2 import views
from django.contrib.auth import views as auth_views
from proj2.views import add_produto, produto_detalhes, buscar_produtos
import sys
sys.path.append(r'C:\Users\jc-noturno\projeto2\projeto22\proj2')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_produto/', add_produto, name='add_produto'),
    path('editar/<int:id>/', views.edit_produto, name='edit_produto'),
    path('remover/<int:id>/', views.delete_produto, name='delete_produto'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('produto/<slug:slug>/', views.produto_detalhes, name='produto_detalhes'),
    path('buscar_produtos/', buscar_produtos, name='buscar_produtos'),
]