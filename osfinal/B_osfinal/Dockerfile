# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy B_osfinal.py
COPY B_osfinal.py .

# Install dependencies
RUN pip install pymongo
RUN pip install confluent-kafka

# Run B_osfinal.py as the entry point
CMD ["python", "B_osfinal.py"]
