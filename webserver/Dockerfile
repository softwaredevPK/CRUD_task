FROM python:3

# Make a directory for our app
WORKDIR /var/www/app

# Copy txt with dependencies
COPY requirements.txt .

# install all dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy code, and project essentials
COPY app ./app

CMD ["uvicorn", "my_api:app", "--host", "0.0.0.0", "--port", "8000"]

