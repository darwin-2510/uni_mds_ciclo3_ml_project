# MLOps Introduction: Final Project
FInal work description in  the [final_project_description.md](final_project_description.md) file.

Student info:
- Full name: Darwin Zavala Paiva
- e-mail: darwin.zavala.p@uni.pe
- Grupo: 2

## Project Name: [Iredit Risk End-to-End Pipeline]

# 1. Descripción del Proyecto
Este proyecto implementa un sistema de clasificación de riesgo crediticio utilizando un enfoque de MLOps. El objetivo principal es transformar un modelo de Machine Learning tradicional en un servicio productivo, auditable y escalable. Se utiliza un dataset de Kaggle para predecir si un préstamo representa un riesgo alto o bajo basándose en el perfil financiero del solicitante.
https://www.kaggle.com/datasets/laotse/credit-risk-dataset

# 2. Arquitectura y Fases Cubiertas
Siguiendo el programa del curso, se completaron las siguientes fases:

    Fase 1: Control de Versiones (Git): Estructuración profesional del repositorio, manejo de ramas (feature/credit-model) y gestión de identidades para trazabilidad de cambios.

    Fase 2: Experimentación (MLflow): Registro de parámetros e hiperparámetros del modelo (Random Forest) y seguimiento de métricas como el Accuracy.

    Fase 3: Serialización: Exportación del modelo entrenado a un formato binario persistente (.joblib) para su posterior consumo.

    Fase 4: Serving (API REST): Desarrollo de un servidor con Flask que expone un endpoint de predicción, permitiendo la interacción con sistemas externos mediante objetos JSON.

    Fase 5: Contenerización (Docker): Creación de un Dockerfile para empaquetar el código, dependencias y modelo, asegurando la portabilidad del sistema.
    You can also use links/reference to other documents/files form this repository or outside resources.

# 3. Bitácora de Implementación (Workflow)
        # Crear y activar entorno virtual
        python -m venv .venv  
        .\.venv\Scripts\activate

        # Instalación de dependencias
        pip install -r requirements_dev.txt
        
        #Pipeline de Ejecución
        EDA:eda_analysis.py
        correlacion_variables.png
        distribucion_riesgo.png
        ingresos_vs_monto.png

        Preparación y Entrenamiento:
        python src/data_preparation.py
        python src/train.py

        #Monitoreo con MLflow:
        Se levantó la UI en el puerto 5001 para evitar conflictos:
        mlflow ui --port 5001
        Visualización disponible en: http://127.0.0.1:5001.

        #Levantamiento de la API:
        python src/serving.py
        Servidor activo en: http://127.0.0.1:5000.

# 4. Pruebas de Inferencia y Resultados
Se validó la API mediante peticiones POST en PowerShell, obteniendo los siguientes resultados según el perfil de riesgo:

Prueba 1: Perfil de Riesgo Bajo
Input: Cliente de 30 años, ingresos de 50,000, monto solicitado 10,000.

Resultado: {"prediction": 0, "status": "Riesgo Bajo"}.

Prueba 2: Perfil de Riesgo Alto
Input: Cliente de 18 años, ingresos de 10,000, monto solicitado 30,000.

Resultado: {"prediction": 1, "status": "Riesgo Alto"}.

# 5. Archivos Generados
models/credit_model.joblib: Binario del modelo entrenado.

mlruns/: Directorio con metadatos y artefactos de experimentos de MLflow.

Dockerfile: Configuración para despliegue en contenedores.

requirements_dev.txt: Lista de librerías necesarias (Pandas, Scikit-learn, MLflow, Flask).
