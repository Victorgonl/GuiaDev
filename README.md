# GuiaDev

Um projeto de Programação WEB

# Ambiente de desenvolvimento

- Sistema Operacional: Linux

## pip & venv

Certifique que os pacotes `python3-pip` e `python3-venv` estão deviamente instalados.

    sudo apt install python3-pip

<p></p>

    sudo apt install python3-venv

## Graphviz (para diagrama relacioanal do modelo de dados)

O pacote `graphviz` servirá para extrair o modelo relacional do banco de dados da aplicação.

    sudo apt install graphviz

## Ambiente virtual

A criação e ativação do ambiente virtual Python é feita pelo comando:

    python3 -m venv .venv

<p></p>

    source .venv/bin/activate

## Pacotes Python

Os pacotes `pip` estão disponíveis no arquivo `./requirements.txt` e pode ser instalado com:

    pip install -r requirements.txt

## Rabbitmq

O Sistema de Mensageria utilizado para comunicar entre a aplicação WEB `GuiaDev` e o serviço de e-mail `GuiaDev E-mail` é o `RabbitMQ`. Os comandos abaixo utilizam o script `rabbitmq.sh` para instalar o serviço. Posteriormente, susbtituímos por um `container` `Docker`.

### Instalar Rabbitmq

    cd rabbitmq

    chmod +x ./rabbitmq.sh

    sudo ./rabbitmq.sh

### Start server

    sudo systemctl start rabbitmq-server

### Stop server

    sudo systemctl stop rabbitmq-server

## GuiaDev (Aplicação WEB)

A Aplicação WEB está implementada em `./guiadev`.

A aplicação não depende do `GuiaDev E-mail` ou `RabbitMQ` para funcionar, exceto seu recurso de envio de e-mail, que utiliza o Sistema de Mensageria para enviar a mensagem para o `GuiaDev E-mail`. Mas caso um dos dois estiver indisponível, não irá afetar seu funcionamento.

    cd guiadev

### Execução

O seguinte comando inicia o servidor `Django`:

    python3 manage.py runserver

### Atualizar banco de dados

Para analisar alterações no modelo de dados e aplicar as alterações no banco de dados, utilizamos o par de comandos:

    python3 manage.py makemigrations

<p></p>

    python3 manage.py migrate

### Criação de administrador

Para criarmos administradores do servidor, utilizamos:

    python3 manage.py createsuperuser

### Diagrama Relacional dos Modelos

O comando a seguir atualiza a imagem do modelo de dados:

    python3 manage.py graph_models base -g -o ../relational_model.png

<img src="./relational_model.png">

## GuiaDev E-mail (Serviço de E-mail)

A implementação do serviço de e-mail está disponível em `./guiadev-email`. O serviço é independente da aplicação WEB, não requerindo seu funcionamento, mas é dependendo do serviço do `RabbitMQ`.

    cd guiadev-email

### Execução

Para executar o serviço:

    python3 guiadev-email.py

# Docker

A seguir, iremos executar nossa aplicações e o `RabbitMQ` utilizando `Docker`.

## Instalação

### Docker Engine & Docker Compose Plugin

    sudo apt-get update

<p></p>

    sudo apt-get install ca-certificates curl gnupg

<p></p>

    sudo install -m 0755 -d /etc/apt/keyrings

<p></p>

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

<p></p>

    sudo chmod a+r /etc/apt/keyrings/docker.gpg

<p></p>

    echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

<p></p>

    sudo apt-get update

<p></p>

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

<p></p>

## Criação de grupo para acessar recursos do `Docker`

Criamos o grupo de usuários `docker` se já não estiver criado e adicionamos o usuário atual `$USER`.

    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker

## Criação de uma network

Iremos criar uma network exclusiva para nossas aplicações: `guiadev-network`.

    docker network create guiadev-network

Podemos verificar as networks criadas com o comando:

    docker network ls

## `Dockerfile`

Iremos definir três imagens para `GuiaDev`, `GuiaDev E-mail` e `RabbitMQ`, cada uma em seu diretório específico.

## Build

Para criarmos cada uma das imagens definidas, utilizamos:

- `GuiaDev`:

      docker build -t guiadev ./guiadev

- `GuiaDev E-mail`:

      docker build -t guiadev-email ./guiadev-email

- `RabbitMQ`:

      docker build -t guiadev-rabbitmq ./rabbitmq

## Run

Para iniciar um container para cada aplicação, utilizamos:

- `GuiaDev`:

      docker run -d --name guiadev --network=guiadev-network -p 8000:8000 guiadev

- `RabbitMQ`:

      docker run -d --name guiadev-rabbitmq --network=guiadev-network -p 5672:5672 -p 15672:15672 guiadev-rabbitmq

- `GuiaDev E-mail`:

      docker run -d --name guiadev-email --network=guiadev-network guiadev-email

É importante que o container do `RabbitMQ` seja iniciado antes do container do `GuiaDev E-mail`.

## `Docker Compose`

Podemos utilizar `docker-compose.yml` para criar as imagens e todas as aplicações utilizando:

    docker compose up -d

#

## Rodar o projeto com docker container por container

# Criar subnet

    docker network create --subnet=172.18.0.0/16 guiadevnet

# Fazer build da imagem do rabbitmq

    Na pasta ./rabbitmq
    docker build -t rabbitmq .

# Subir container com o Rabbitmq na network criada com ip statico

    docker run --net=guiadevnet --ip=172.18.0.22 -it rabbitmq

# Fazer build da imagem do enviador de email

    Na pasta ./guiadev-email

    docker build -t email

# Subir o container com o email

    docker run -it email

# Fazer build da imagem do guiadev-web

    Na pasta ./guiadev
    docker build -t guidev .

    # Subir o container com a imagem guiadev mapeando a
    porta 8080 do localhost com a porta 8000 do container

    docker run -it -p 8080:8000 guiadev

## Rodar o projetor com docker compose

    #Especificando o arquivo compose com -f
      docker compose -f docker-compose.yml up

    #Utilizando o .yml no diretório local
      docker compose up

## Listar networks

    docker network ls

## Verificar info da network no docker

    docker network inspec [nome_network]

## Listar containes

    docker container ls

## Listar imagens

    docker images

## Deletar imagens

    docker rmi

## Apagar cache do docker

    docker system prune

## Comando docker para ver ip do container

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [CONTAINER-ID] #Verifica ip do container

## Curiosidades sobre docker

É feito na linguam Go.
