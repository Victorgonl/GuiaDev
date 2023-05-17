# Projeto de Programção WEB

# Ambiente (Ubuntu)

## pip & venv

    sudo apt install python3-pip

    sudo apt install python3-venv

## Ambiente virtual

    python3 -m venv .venv

    source .venv/bin/activate

    cd Projeto

## Pacotes Python

    pip install django

    pip install pyperclip

# Aplicação

## Execução do servidor

    python3 manage.py runserver

## Criação do banco de dados

    python3 manage.py migrate

## Atualização no banco de dados

    python3 manage.py makemigrations polls

    python3 manage.py sqlmigrate polls 0001

## Criação de administrador

    python manage.py createsuperuser