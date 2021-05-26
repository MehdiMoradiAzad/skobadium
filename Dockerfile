FROM python:slim

LABEL maintainer="Mehdi Moradi Azad <MehdiMoradiAzad@gmail.com>"

EXPOSE 8080

WORKDIR /opt/app

ENV SKOB_AUTHZ_BIND_ADDRESS=0.0.0.0
ENV SKOB_AUTHZ_NUM_WORKERS=4

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN useradd -M -d /opt/app authz
USER authz

CMD ./start
