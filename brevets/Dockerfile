FROM python:3.8
LABEL maintainer="kpinkham13@gmail.com"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
