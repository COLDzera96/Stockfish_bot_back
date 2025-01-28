# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

# Make the Stockfish binary executable
RUN chmod +x stockfish/stockfish-ubuntu-x86-64-avx2

# Expose the port the app runs on
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]