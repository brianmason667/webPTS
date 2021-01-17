FROM php:7.3-apache
#COPY ./src/ /var/www/html/
EXPOSE 80/tcp
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
RUN docker-php-ext-configure mysqli
RUN docker-php-ext-install mysqli
RUN service apache2 restart
