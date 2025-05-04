# Use official Python base image
FROM python:3.10-slim

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies and Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    poppler-utils \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy your app code and requirements
COPY . /app

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional, for docs)
EXPOSE 10000

# Set environment variable for tesseract path (pytesseract needs this)
ENV TESSERACT_CMD=/usr/bin/tesseract

# Run the Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
