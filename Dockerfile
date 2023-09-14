FROM python:3.10.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "PizzaShop.wsgi:application"]
