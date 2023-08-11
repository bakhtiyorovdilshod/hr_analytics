# Dockerfile

# Use the official Python image as a base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code and requirements into the container
COPY . /app
COPY ./requirements.txt /app

# Install the required dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "9000"]
