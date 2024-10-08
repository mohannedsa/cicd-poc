# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app/app

# Copy the current directory contents into the container at /app
COPY . /app/app

# Install any needed packages specified in requirements.txt
RUN pip3 install flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]