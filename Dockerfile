# Use the official Python 3.10 image as base
FROM python:3.10.13-alpine

# Set maintainer label
LABEL maintainer="abdallah nasir"

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PATH="/venv/bin:$PATH"

# Install system dependencies
RUN apk add --no-cache \
    build-base \
    gdal gdal-dev \
    gettext \
    libffi-dev \
    libxml2 \
    libxslt-dev \
    pango \
    shared-mime-info \
    ca-certificates \
    && update-ca-certificates \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    musl-dev \
    postgresql-dev \
  && apk del .build-deps

# Create and activate virtual environment
RUN python -m venv /venv

# Upgrade pip
RUN pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for running the application
RUN adduser -D django-user
USER django-user

# Copy the application code
COPY . /app

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
