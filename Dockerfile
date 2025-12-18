# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
RUN pip install pandas openpyxl

# Copy the python scripts to the container
COPY main.py .
COPY saving_password.py .

# Command to run the script
CMD ["python", "main.py"]