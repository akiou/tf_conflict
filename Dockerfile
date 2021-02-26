FROM python:3.6-stretch

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV JDK_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PYTHONPATH /src

WORKDIR /src
COPY requirements.txt /src

RUN apt-get update && apt-get install -y openjdk-8-jdk maven
RUN pip install -r requirements.txt
