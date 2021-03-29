FROM httpd:2.4
ENV PYTHONUNBUFFERED=1
EXPOSE 8000/tcp
EXPOSE 80/tcp
WORKDIR /code
RUN apt update
RUN apt install -y build-essential python3.7 python3-pip libxml2-dev
RUN ln -s /usr/bin/python3.7 /usr/bin/python
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN echo 'LoadModule rewrite_module modules/mod_rewrite.so' >> /usr/local/apache2/conf/httpd.conf
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
