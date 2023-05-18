# Projeto de Programção WEB

# Ambiente (Linux)

## pip & venv

    sudo apt install python3-pip

<p></p>

    sudo apt install python3-venv

## Ambiente virtual

    python3 -m venv .venv

<p></p>

    source .venv/bin/activate

## Pacotes Python

    pip install -r requirements.txt

# Aplicação

## Execução do servidor

    python3 manage.py runserver

## Criação do banco de dados

    python3 manage.py migrate

## Atualização no banco de dados

    python3 manage.py makemigrations polls

<p></p>

    python3 manage.py sqlmigrate polls 0001

## Criação de administrador

    python3 manage.py createsuperuser