# Use an official Python runtime as a parent image
FROM python:3-alpine3.15



# Set the working directory in the container
WORKDIR /app



# Install Python dependencies
COPY . /app
RUN pip install -r requirements.txt


# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]