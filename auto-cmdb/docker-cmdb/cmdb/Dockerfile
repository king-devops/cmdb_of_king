FROM centos7:v1
RUN python3 /opt/auto_cmdb/manage.py makemigrations && python3 /opt/auto_cmdb/manage.py migrate
CMD uwsgi --ini /opt/auto_cmdb/conf/uwsgi.ini 