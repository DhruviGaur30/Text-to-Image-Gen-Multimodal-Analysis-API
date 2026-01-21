# ------------------------------
# Base image
# ------------------------------
FROM python:3.11-slim

# ------------------------------
# Environment variables
# ------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ------------------------------
# System dependencies
# ------------------------------
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------
# Working directory
# ------------------------------
WORKDIR /app

# ------------------------------
# Copy requirements
# ------------------------------
COPY requirements.txt .

# ------------------------------
# Install Python dependencies
# ------------------------------
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ------------------------------
# Copy application code
# ------------------------------
COPY . .

# ------------------------------
# Expose API port
# ------------------------------
EXPOSE 8000

# ------------------------------
# Run FastAPI app
# ------------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
