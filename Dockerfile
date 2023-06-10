# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the necessary files and directories to the container
COPY ./gpt /app/gpt
COPY api.py /app
COPY setup.py /app
COPY upload_epub.py /app
COPY __main__.py /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run when the container starts
CMD ["python", "__main__.py"]