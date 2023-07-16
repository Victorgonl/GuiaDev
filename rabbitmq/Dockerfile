# ==================== guiadev-rabbitmq ==================== #


# Criar esta imagem: docker build -t guiadev-rabbitmq .
# Executar esta imagem: docker run -d --name guiadev-rabbitmq --network=guiadev-network -p 5672:5672 -p 15672:15672 guiadev-rabbitmq
# Acessar RabbitMQ: http://localhost:15672/


# Imagem oficial do RabbitMQ
FROM rabbitmq:3.12-management

# Porta
EXPOSE 5672 15672

# Set the RabbitMQ environment variables
ENV RABBITMQ_DEFAULT_USER=guiadev
ENV RABBITMQ_DEFAULT_PASS=guiadev

# Enable the RabbitMQ management plugin
RUN rabbitmq-plugins enable rabbitmq_management

# Start the RabbitMQ server
CMD ["rabbitmq-server"]