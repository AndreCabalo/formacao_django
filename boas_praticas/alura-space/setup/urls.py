from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('galeria.urls'))           #Adicionamos o caminho a index
]


