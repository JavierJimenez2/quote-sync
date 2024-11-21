

# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Define the port to replace in the .env file
ARG FRONTEND_PORT=5173

# Update the .env file with the correct FRONTEND_PORT
RUN echo "CORS_ALLOWED_ORIGINS=http://localhost:8000,http://frontend:${FRONTEND_PORT}" > .env

# Expose the port
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
