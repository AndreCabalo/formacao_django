from django.shortcuts import render

# 2- Criamos um função que faz com que aparece o comando htlm com Alura Space 
def index(request):
    return render(request, 'galeria/index.html') #usando sempre o render, tendo o primeiro parametro sempre request, apontamos o nome do arquivo

def imagem(request):
    return render(request, 'galeria/imagem.html') 