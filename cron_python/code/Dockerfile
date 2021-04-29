FROM ubuntu:20.04

# Instalo componentes
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && apt-get -y install cron && apt-get install vim -y \
  && pip3 --no-cache-dir install --upgrade pip
 
# Creo directorio de trabajo:
WORKDIR /code

# agrego cron al directorio
COPY crontab /etc/cron.d/crontab

# Copio archivos / scripts
COPY . /code/

# Asgino permisos de ejecucion
RUN chmod +x /code/script.sh
RUN chmod +x /code/script.py

RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["cron", "-f"]