FROM httpd:2.4
ENV PYTHONUNBUFFERED=1
EXPOSE 8000/tcp
EXPOSE 80/tcp
WORKDIR /code
RUN apt update
RUN apt install -y build-essential python3.7 python3-pip libxml2-dev
RUN ln -s /usr/bin/python3.7 /usr/bin/python
COPY requirements.txt /code/
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

