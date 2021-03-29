FROM python:3
ENV PYTHONUNBUFFERED=1
EXPOSE 8000/tcp
EXPOSE 80/tcp
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y build-essential
RUN apt install -y apache2 libxml2-dev
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_ajp
RUN a2enmod rewrite
RUN a2enmod deflate
RUN a2enmod headers
RUN a2enmod proxy_balancer
RUN a2enmod proxy_connect
RUN a2enmod proxy_html
RUN a2enmod proxy_wstunnel
RUN chown -R root:root /var/www/html/*
COPY 000-default.conf /etc/apache2/sites-enabled/
RUN mkdir /var/www/html/static
RUN update-rc.d apache2 defaults
RUN /etc/init.d/apache2 start
#COPY . /code/
