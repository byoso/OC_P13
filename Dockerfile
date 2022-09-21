# Reminder
# build: docker build --build-arg port=8000 -t heroku-django:v1 .
# run: docker run --rm -p 8000:8000 heroku-django:v1


# Base image
FROM python:3.10-slim-buster
ARG port

USER root

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=$port

# Working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . .

EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT project_core.wsgi:application
