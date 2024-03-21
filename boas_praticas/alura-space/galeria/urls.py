# Iremos importar:
from django.urls import path
from galeria.views import index,imagem

# Criaremos um lista de urls, que a importaremos la para setup urls.py
urlpatterns = [
    path('',index, name='index'),
    path('imagem/',imagem, name='imagem')
]