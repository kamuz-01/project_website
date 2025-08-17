from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def especialidades(request):
    return render(request, 'website/especialidades.html')

def sobre(request):
    return render(request, 'website/sobre.html')

def contato(request):
    return render(request, 'website/contato.html')
