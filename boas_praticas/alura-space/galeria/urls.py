# Iremos importar:
from django.urls import path
from galeria.views import index

# Criaremos um lista de urls, que a importaremos la para setup urls.py
urlpatterns = [
    path('',index)
]