FROM mysql:8

#####################################
# Set Timezone
#####################################

ARG TZ=UTC
ENV TZ ${TZ}
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN chown -R mysql:root /var/lib/mysql/
#CMD ["mysqld"]
EXPOSE 3306