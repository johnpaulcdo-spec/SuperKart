# ✅ Use a minimal Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from local deployment folder into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 7860

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
