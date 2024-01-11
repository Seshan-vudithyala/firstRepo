# Dockerfile
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y python3 python3-pip gunicorn && pip install -r requirements.txt
#env
ENV NAME PythonENV
EXPOSE 8080
# Run app.py when the container launches
CMD gunicorn -b 0.0.0.0:8080 app:server
