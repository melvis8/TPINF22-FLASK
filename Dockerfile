# Dockerfile pour Flask + PostgreSQL

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.run
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=/app


CMD ["flask", "run"]
