# GuiaDev

Um projeto de Programação WEB

# Ambiente (Linux)

## pip & venv

    sudo apt install python3-pip

<p></p>

    sudo apt install python3-venv

## Graphviz

    sudo apt install graphviz

## Ambiente virtual

    python3 -m venv .venv

<p></p>

    source .venv/bin/activate

## Pacotes Python

    pip install -r requirements.txt

# Aplicação

    cd guiadev

## Execução do servidor

    python3 manage.py runserver

## Habbitmq
  
  #Start server 

    sudo systemctl start rabbitmq-server
  
  #Stop server 

    sudo systemctl stop rabbitmq-server

  #Criar fila

    rabbitmqadmin -u {user} -p {password} -V {vhost} declare queue name={name}

## Banco de dados

    python3 manage.py makemigrations

<p></p>

    python3 manage.py migrate

## Criação de administrador

    python3 manage.py createsuperuser

# Diagrama Relacional dos Modelos

    ./guiadev/manage.py graph_models base -g -o relational_model.png

<img src="./relational_model.png">