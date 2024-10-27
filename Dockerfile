# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (default to 8080 for Render)
EXPOSE 8080

# Run the Flask server
CMD ["python", "src/server.py"]
