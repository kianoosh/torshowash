FROM python:3.12-alpine3.13
LABEL maintainer="kianoosh.koochaki@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp//requirements.txt 
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    /env/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disable-password \
        --no-create-home \
        django-user

ENV PATH="/env/bin:$PATH"

USER django-user