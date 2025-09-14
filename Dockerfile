FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app directly (no training at build)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

