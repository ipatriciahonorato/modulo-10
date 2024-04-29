# Use a base image with Python 3.10
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into our working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY src/ .

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
