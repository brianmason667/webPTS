FROM php:7.3-apache
#this will copy insted of mount the webroot
#COPY ./www/ /var/www/html/
EXPOSE 80/tcp
RUN cp "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
RUN docker-php-ext-configure mysqli
RUN docker-php-ext-install mysqli
RUN service apache2 restart
