# Reminder
# build: docker build -t oc_lettings_site:v1 .
# run: docker run --rm -p 8000:8000 oc_lettings_site:v1


# Base image
FROM python:3.10-slim-buster

# USER root

# Environment variables
ENV PORT=8000

# Working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -U pip \
    && pip install -r requirements.txt

# Copy project
COPY . .

# Collect the statics
RUN python manage.py collectstatic --no-input

EXPOSE $PORT

# Run the project
CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi:application
