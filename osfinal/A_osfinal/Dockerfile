# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy A_osfinal.py
COPY A_osfinal.py .

# Install dependencies
RUN pip install pymongo
RUN pip install confluent-kafka

# Run A_osfinal.py as the entry point
CMD ["python", "A_osfinal.py"]
