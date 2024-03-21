# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files to the working directory
COPY app.py .
COPY score.py .
COPY model.pkl .

# Expose the Flask app port
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "app.py"]
