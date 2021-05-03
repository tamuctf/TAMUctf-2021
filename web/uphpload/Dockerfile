FROM alpine


RUN apk --update add apache2 php7 php7-apache2 php7-session


env APACHE_RUN_USER    www-data
env APACHE_RUN_GROUP   www-data
env APACHE_PID_FILE    /var/run/apache2.pid
env APACHE_RUN_DIR     /var/run/apache2
env APACHE_LOCK_DIR    /var/lock/apache2
env APACHE_LOG_DIR     /var/log/apache2

EXPOSE 80

COPY start.sh /start.sh
COPY index.php /var/www/localhost/htdocs/index.php
COPY upload.php /var/www/localhost/htdocs/upload.php
COPY uploads /var/www/localhost/htdocs/uploads
RUN chgrp www-data /var/www/localhost/htdocs/uploads
RUN chmod g+w /var/www/localhost/htdocs/uploads
RUN rm /etc/apache2/httpd.conf
COPY httpd.conf /etc/apache2/httpd.conf

RUN mkdir /flag_is_here
COPY flag.txt /flag_is_here/flag.txt

ENTRYPOINT ["sh", "start.sh"]
