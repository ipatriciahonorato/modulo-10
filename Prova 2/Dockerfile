# Use the official Python image.
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code
COPY / .

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
