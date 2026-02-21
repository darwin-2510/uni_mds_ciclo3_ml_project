import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. Configuración de rutas
data_path = 'data/raw/credit_risk_dataset.csv' 
reports_path = 'reports/images/'

if not os.path.exists(reports_path):
    os.makedirs(reports_path)

# 2. Carga de datos
df = pd.read_csv(data_path)

# --- VISTA 1: Distribución de la variable objetivo ---
plt.figure(figsize=(8, 6))
sns.countplot(x='loan_status', data=df, palette='viridis')
plt.title('Distribución de Riesgo Crediticio (0: Bajo, 1: Alto)')
plt.savefig(f'{reports_path}distribucion_riesgo.png')
plt.close()

# --- VISTA 2: Relación Ingresos vs Monto del Préstamo ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='person_income', y='loan_amnt', hue='loan_status', data=df, alpha=0.5)
plt.title('Ingresos vs Monto del Préstamo por Estado de Riesgo')
plt.savefig(f'{reports_path}ingresos_vs_monto.png')
plt.close()

# --- VISTA 3: Mapa de Calor de Correlación ---
plt.figure(figsize=(12, 8))
correlation = df.select_dtypes(include=['number']).corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación de Variables Financieras')
plt.savefig(f'{reports_path}correlacion_variables.png')
plt.close()

print(f"Análisis completado. Imágenes guardadas en: {reports_path}")