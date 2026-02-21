from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo al iniciar el servidor
model = joblib.load("models/credit_model.joblib")

@app.route("/predict", methods=["POST"]) # Decorador de ruta
def predict():
    # Obtener datos del cliente (Lección 5 - Request object)
    data = request.get_json()
    df_input = pd.DataFrame([data])
    
    # Inferencia
    prediction = model.predict(df_input)
    result = "Riesgo Alto" if prediction[0] == 1 else "Riesgo Bajo"
    
    return jsonify({"prediction": int(prediction[0]), "status": result})

if __name__ == "__main__":
    app.run(port=5000, debug=True)