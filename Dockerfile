# Use a lightweight Python 3.8 image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt requirements.txt

# Install dependencies and clean up to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "api/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
