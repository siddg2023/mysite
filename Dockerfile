# # Use an official Python runtime as a parent image
# FROM python:3.8

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /mysite

# # Copy the requirements file into the container at /mysite/
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /mysite/
# COPY . .

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /mysite

# Copy the requirements file into the container at /mysite/
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /mysite/
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

