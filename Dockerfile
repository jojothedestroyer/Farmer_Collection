# ARG PYTHON_VERSION=3.10-slim-bullseye
# FROM python:${PYTHON_VERSION}

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Install necessary system packages
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     pkg-config \
#     libcairo2-dev \
#     gcc \
#     build-essential && \
#     rm -rf /var/lib/apt/lists/*

# # Create and set the working directory
# RUN mkdir -p /code
# WORKDIR /code

# # Install Python dependencies
# COPY requirements.txt /tmp/requirements.txt
# RUN set -ex && \
#     pip install --upgrade pip && \
#     pip install -r /tmp/requirements.txt && \
#     rm -rf /root/.cache/

# # Copy the application code
# COPY . /code

# # Expose the application port
# EXPOSE 8000

# # Command to run the application
# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "GCNA_db.wsgi:app"]
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential libcairo2-dev pkg-config

# Create and set working directory
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# Expose port
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "GCNA_db.wsgi:app"]
