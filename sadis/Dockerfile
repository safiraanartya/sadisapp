# Pilih image dasar yang memiliki Python
FROM python:3.9-slim

# Set working directory
 WORKDIR /

# Salin file aplikasi Anda ke dalam container
 COPY . /

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan perintah migrate Django
RUN python manage.py migrate

# Tentukan perintah untuk menjalankan aplikasi
CMD ["python", "manage.py", "runserver", "0.0.0.0:3306"]
