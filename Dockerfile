# Usar una imagen oficial de Python como base
FROM python:3.11-slim

# Establecer variables de entorno
# Evita que Python genere archivos .pyc en el contenedor
ENV PYTHONDONTWRITEBYTECODE 1
# Asegura que la salida de Python se envíe directamente a la terminal sin ser almacenada en el búfer
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos e instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto al directorio de trabajo
COPY . /app/

# Exponer el puerto en el que corre Django
EXPOSE 8000

# Recopilar archivos estáticos para producción
RUN python manage.py collectstatic --noinput

# Comando para ejecutar la aplicación con Gunicorn en producción
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend_red_social.wsgi:application"]
