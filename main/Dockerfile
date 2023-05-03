FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip && pip install --upgrade setuptools
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update -y && \ 
    apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev && \
    pip install python-ldap==3.3.1
RUN pip install --no-cache -r requirements.txt
COPY . /app