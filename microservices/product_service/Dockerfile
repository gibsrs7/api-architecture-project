# Use an official, lightweight Python image as the base.
# 'python:3.9-slim' is a good choice as it's smaller than the full version.
FROM python:3.9-slim

# Set the working directory inside the container to /app.
# All subsequent commands will run from this directory.
WORKDIR /app

# Copy the requirements file into the container at /app/requirements.txt
COPY requirements.txt .

# Run the pip install command inside the container to install our dependencies.
# --no-cache-dir makes the image a bit smaller.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our application's source code from the host
# into the container's /app directory.
COPY . .

# Tell Docker that the container will listen on this port at runtime.
# This is just metadata; it doesn't actually open the port.
EXPOSE 5001

# The command that will be executed when the container starts.
# This runs our application.
CMD ["python", "product_service.py"]