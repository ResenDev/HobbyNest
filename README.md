
# 🗄 HobbyNest

![Static Badge](https://img.shields.io/badge/License-Apache%202.0-red)

O **HobbyNest** é um sistema web desenvolvido para que os usuários possam gerenciar e explorar seus acervos pessoais de forma prática e organizada. O sistema permite manipular a lista dos itens que já possuem, para um melhor controle. Os itens são classificados em quatro categorias principais: Livros, Cursos, Jogos e Filmes/Séries.


## 🛠️ Stack utilizada

- **Front-end:** Html, Css, Bootstrap e JavaScript.
- **Back-end:** Python, Django e PostgreSQL.

<div class="icons-container"> 

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" alt="html" width="40" height="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" alt="css" width="40" height="40" />                          
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap" width="40" height="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="Javascript" width="40" height="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" alt="django" width="40" height="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original-wordmark.svg" alt="postgres" width="40" height="40" />   
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40" />                 
</div>

## ⚙️ Funcionalidades

- *Autenticação de usuário*: Apenas usuários cadastrados podem acessar o sistema;

- *CRUD de itens*: O usuário pode manipular os itens do seu acervo pessoal;

- *Busca*: A plataforma possui um sistema de busca eficiente, permitindo que o usuário encontre rapidamente itens no acervo por nome;

- *Ordenação*: Ordena por título e por data de atualização;

- *Exportar lista para PDF ou CSV*;

- *Paginação*.

## 📽️ Demonstração

Insira um gif ou um link de alguma demonstração


## 💻 Rodando localmente

Clone esse repositório
```bash
    git clone https://github.com/ResenDev/HobbyNest.git
```

Crie o seu ambiente virtual
```bash
    python -m venv venv
```
Ative seu ambiente virtual

Windows:
```bash
    venv\Scripts\activate
```
Mac/Linux:
```bash
    source venv/bin/activate
```
Navegue até a pasta *app*
```bash
   cd app 
```

Atualize o pip e instale as bibliotecas do *requirements.txt*
```bash
    pip install --upgrade pip
    pip install -r requirements.txt
```
Retorne à pasta anterior 
```bash
    cd ..
```
Renomeie o arquivo de variáveis de ambiente *.env-git*

Windows:
```bash
    ren .env-git .env
```
Mac/Linux:
```bash
    mv .env-git .env
```
Após isso, mude os valores das variáveis do *.env* para os valores do seu banco de dados no arquivo 

Faça as migrações
```bash
   python manage.py makemigrations
   python manage.py migrate 
```
Rode o projeto
```bash
    python manage.py runserver
```


## 🤝 Contribuindo

Contribuições são sempre bem-vindas!

Veja `contribuindo.md` para saber como começar.

Por favor, siga o `código de conduta` desse projeto.


## 👨🏽‍🎨 Autor

<a><img src="https://avatars.githubusercontent.com/u/82344312?v=4" alt="Rafael Resende" width="280" height="280"/></a>

- [Rafael Resende - @ResenDev](https://www.github.com/ResenDev)

