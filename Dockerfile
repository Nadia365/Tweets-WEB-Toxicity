FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system packages
RUN apt-get update && apt-get install -y \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

# Add .env support
ENV BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAHup2AEAAAAAaDJ6uIMAz9m4%2FJIp1tuSqvPQtBA%3Dlx89suzJRbZMQG726y6g5yTkrXQ3Y8Iuj7I5cC0xjmc9dxNsUJ

