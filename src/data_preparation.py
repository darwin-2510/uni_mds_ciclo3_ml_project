import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(path):
    df = pd.read_csv(path)
    # Manejo de nulos (Lección 4 - Preprocesamiento)
    df['person_emp_length'] = df['person_emp_length'].fillna(df['person_emp_length'].median())
    df['loan_int_rate'] = df['loan_int_rate'].fillna(df['loan_int_rate'].median())
    
    # Codificación de categorías
    le = LabelEncoder()
    df['person_home_ownership'] = le.fit_transform(df['person_home_ownership'])
    df['loan_intent'] = le.fit_transform(df['loan_intent'])
    
    # Separación de features y target
    X = df.drop(columns=['loan_status', 'cb_person_default_on_file', 'loan_grade'])
    y = df['loan_status']
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == "__main__":
    # Guardamos la data procesada en data/training/
    X_train, X_test, y_train, y_test = load_and_clean_data("data/raw/credit_risk_dataset.csv")
    X_train.to_csv("data/training/X_train.csv", index=False)
    y_train.to_csv("data/training/y_train.csv", index=False)
    print("Data preparada exitosamente en data/training/")