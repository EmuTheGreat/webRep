FROM python:3.10-slim


WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG DEV=false

RUN pip install --upgrade pip && pip install "poetry==1.4.1"

RUN apt-get update && apt-get install -y build-essential libpq-dev curl make git


RUN pip install psycopg2-binary --no-binary psycopg2-binary

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --without dev

COPY . .

RUN python /app/manage.py collectstatic --noinput
