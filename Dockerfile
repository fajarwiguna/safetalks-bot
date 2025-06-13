# Gunakan base image Python
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy semua file ke container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan bot
CMD ["python", "main.py"]
