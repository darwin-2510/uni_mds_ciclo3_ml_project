# Crear entorno virtual
-m venv .venv  
.\.venv\Scripts\activate

# Crear archivo de req librerias
    # requirements_dev.txt
        pandas
        mlflow
        scikit-learn
        pytest
        flask
        joblib
        mlflow
pip install -r .\requirements.txt    

# Data/Raw
Cargar archivo dataset Test

# Modelos
Crear archivos>
    data_preparation.py
    train.py
    serving.py


# PowerShell
python src/data_preparation.py
python src/train.py

# Levantar API

mlflow ui --port 5001

Abrir link:
http://127.0.0.1:5001


Abrir una segunda pestaña de la terminal

python src/serving.py

Esto iniciará el servidor de Flask. La terminal se quedará "bloqueada" indicando que el servidor está corriendo en http://127.0.0.1:5000.

# Visualizar Experimento (MLflow UI)
En una tercera termnal"\:

PRUEBA 1:

Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Body '{"person_age": 30, "person_income": 50000, "person_home_ownership": 1, "person_emp_length": 5, "loan_intent": 2, "loan_amnt": 10000, "loan_int_rate": 11.5, "loan_percent_income": 0.2, "cb_person_cred_hist_length": 2}' -ContentType "application/json"

Resultado:
prediction status     
---------- ------
         0 Riesgo Bajo

PRUEBA 2:
Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -Body '{"person_age": 18, "person_income": 10000, "person_home_ownership": 0, "person_emp_length": 0, "loan_intent": 1, "loan_amnt": 30000, "loan_int_rate": 20.0, "loan_percent_income": 0.8, "cb_person_cred_hist_length": 1}' -ContentType "application/json"

prediction status     
---------- ------
         1 Riesgo Alto

# Creacion del archivo Dockerfile


# Actualizar:
git config --global user.email "tu_correo@ejemplo.com"
git config --global user.name "Tu Nombre"

# 1. Preparar los archivos
git add Dockerfile src/serving.py src/train.py src/data_preparation.py models/credit_model.joblib

# 2. Hacer el commit con un mensaje profesional (siguiendo convenciones)
git commit -m "feat: complete ml lifecycle with dockerization and serving"

# 3. Subir la rama al servidor
git push origin feature/credit-model