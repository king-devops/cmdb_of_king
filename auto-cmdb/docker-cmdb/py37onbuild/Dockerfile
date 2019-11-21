FROM centos7-python3.7
ONBUILD COPY . /opt/
ONBUILD RUN pip3 install -r /opt/requirements.txt && pip3 install uwsgi
 
