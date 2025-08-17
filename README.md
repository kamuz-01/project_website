# Atividade para a disciplina PROGRAMAÇÃO WEB II do Instituto Federal Catarinense - Campus Fraiburgo.

## Requisitos para realizar o projeto:

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* GIT - Conferir a instalação: git -v

## Sequencia para criar o projeto

### Criar o ambiente virtual

* python -m venv venv

### Ativar o ambiente virtual no windows

* venv\Scripts\Activate

### Com o venv ativado, instalar o Django

* pip install Django

### Criar o projeto com Django

django-admin startproject project_website .

### Criar app pagina_inicial

* python manage.py startapp website

### Configurar o projeto (views e rotas)

#### Adicionar 'website' ao INSTALLED_APPS em project_website/settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

```

#### Mais abaixo, em project_website/settings.py, adicionar a seguinte linha:

```
STATICFILES_DIRS = [BASE_DIR / 'static']

```

#### Crie as views em project_website/website/views.py

```
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

```

### Crie urls.py em project_website/website/

```
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
```

### Atualize project_website/urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), # redireciona para o app website
]

```

### Criar as paginas html em project_website\website\templates\website; que neste caso foram as seguintes:

- home.html
- sobre-mim.html
- especialidades.html
- contato.html

### criar a pasta static em project_website e dentro dessa pasta static, colocar as pastas:

- css
- imagens
- js

#### As pastas mencionadas anteriormente servirão para adicionar os arquivos css, imagens e javascript respectivamente. 

## Como rodar o projeto baixado

### No terminal, em project_website/ executar o seguinte comando:

```
python manage.py runserver
```

Acessar as páginas criadas com Django.
```
http://127.0.0.1:8000/

```
