from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'paginas/home.html')

def registro(request):
    return render(request, 'paginas/registro.html')