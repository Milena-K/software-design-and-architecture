# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code
COPY . .

RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on
EXPOSE 5005

# Run the Flask app
CMD ["python", "db_api.py"]
