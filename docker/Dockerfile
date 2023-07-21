# Use a imagem base do PHP que contém o Apache e o PHP 7.4
FROM php:7.4-apache
#python install
RUN apt-get update && apt-get install -y python3
# Instalação do pip
RUN apt-get install python3-pip -y && pip3 install requests
RUN pip install schedule
# Define o comando padrão para iniciar o cron e o Apache
CMD ["sh", "-c", "apache2-foreground"]
