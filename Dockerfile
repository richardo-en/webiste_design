# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Node.js and npm
RUN apk add --no-cache nodejs npm

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install any needed JavaScript packages
RUN npm install --package-lock-only

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "website_design/app.py"]
