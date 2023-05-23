#!/bin/sh

if [ -f ".venv/bin/django-admin" ]; then
    echo "Execução do servidor: python3 manage.py runserver"
    echo "Atualizar banco de dados: python3 manage.py makemigrations && python3 manage.py migrate"
    cd src
    exec bash
else
    echo "Comandos para criação do ambiente:"
    echo "python3 -m venv .venv"
    echo "source .venv/bin/activate"
    echo "pip install -r requirements.txt"
    echo "cd src"
    exec bash
fi
