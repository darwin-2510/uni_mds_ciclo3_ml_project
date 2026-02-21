# 1. Usar una imagen base de Python 
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos de requerimientos e instalarlos
COPY requirements_dev.txt .
RUN pip install --no-cache-dir -r requirements_dev.txt

# 4. Copiar las carpetas necesarias para que la API funcione
COPY src/ ./src/
COPY models/ ./models/

# 5. Exponer el puerto donde corre Flask
EXPOSE 5000

# 6. Comando para iniciar la API cuando el contenedor arranque
CMD ["python", "src/serving.py"]