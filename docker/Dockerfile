# Use a imagem base do PHP que contém o Apache e o PHP 7.4
FROM php:7.4-apache
#python install
RUN apt-get update && apt-get install -y python3
# Instalação do pip
RUN apt-get install python3-pip -y && pip3 install requests
RUN pip install schedule
#  command: sh -c "cd /var/www/html/ && python3 cronjob.py"
CMD sh -c "python3 cronjob.py & apache2-foreground"