"""
Script de prédiction de churn pour nouveaux clients
"""

import joblib
import pandas as pd
import numpy as np

def load_model():
    """Charge le modèle et ses métadonnées"""
    model = joblib.load('models/xgboost_churn_model.pkl')
    model_info = joblib.load('models/model_info.pkl')
    return model, model_info

def predict_churn(customer_data):
    """
    Prédit le churn pour un ou plusieurs clients
    
    Args:
        customer_data: DataFrame avec les features nécessaires
        
    Returns:
        predictions: 0 (reste) ou 1 (part)
        probabilities: probabilité de churn
    """
    model, info = load_model()
    
    # Vérifier que toutes les features sont présentes
    required_features = info['features']
    
    # Prédictions
    predictions = model.predict(customer_data[required_features])
    probabilities = model.predict_proba(customer_data[required_features])[:, 1]
    
    return predictions, probabilities

def predict_single_customer(credit_score, gender, age, tenure, balance, 
                           num_products, has_credit_card, is_active, 
                           salary, geography):
    """
    Prédit le churn pour un seul client
    
    Args:
        credit_score: Score de crédit (350-850)
        gender: 0 = Male, 1 = Female
        age: Age du client
        tenure: Années client (0-10)
        balance: Solde du compte
        num_products: Nombre de produits (1-4)
        has_credit_card: 0 ou 1
        is_active: 0 = Inactif, 1 = Actif
        salary: Salaire estimé
        geography: 'France', 'Germany', ou 'Spain'
    
    Returns:
        prediction: 0 ou 1
        probability: probabilité de churn (0-1)
        risk_level: 'Faible', 'Moyen', ou 'Elevé'
    """
    
    # Encoder la géographie
    geo_france = 1 if geography == 'France' else 0
    geo_germany = 1 if geography == 'Germany' else 0
    geo_spain = 1 if geography == 'Spain' else 0
    
    # Créer le DataFrame
    customer_df = pd.DataFrame({
        'CreditScore': [credit_score],
        'Gender': [gender],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'Num Of Products': [num_products],
        'Has Credit Card': [has_credit_card],
        'Is Active Member': [is_active],
        'Estimated Salary': [salary],
        'Geography_France': [geo_france],
        'Geography_Germany': [geo_germany],
        'Geography_Spain': [geo_spain]
    })
    
    # Prédiction
    prediction, probability = predict_churn(customer_df)
    
    # Niveau de risque
    if probability[0] < 0.3:
        risk_level = 'Faible'
    elif probability[0] < 0.6:
        risk_level = 'Moyen'
    else:
        risk_level = 'Elevé'
    
    return prediction[0], probability[0], risk_level


if __name__ == "__main__":
    # Exemple de prédiction
    print("=== Test de Prédiction ===\n")
    
    # Client 1: Profil à risque (femme allemande 55 ans inactive)
    pred, prob, risk = predict_single_customer(
        credit_score=650,
        gender=1,  # Female
        age=55,
        tenure=5,
        balance=100000,
        num_products=2,
        has_credit_card=1,
        is_active=0,  # Inactive
        salary=80000,
        geography='Germany'
    )
    
    print("Client 1 (Femme allemande 55 ans inactive):")
    print(f"  Prédiction: {'CHURN' if pred == 1 else 'RESTE'}")
    print(f"  Probabilité de churn: {prob*100:.1f}%")
    print(f"  Niveau de risque: {risk}")
    
    print("\n" + "="*50 + "\n")
    
    # Client 2: Profil sûr (homme français jeune actif)
    pred2, prob2, risk2 = predict_single_customer(
        credit_score=700,
        gender=0,  # Male
        age=30,
        tenure=8,
        balance=50000,
        num_products=2,
        has_credit_card=1,
        is_active=1,  # Active
        salary=60000,
        geography='France'
    )
    
    print("Client 2 (Homme français 30 ans actif):")
    print(f"  Prédiction: {'CHURN' if pred2 == 1 else 'RESTE'}")
    print(f"  Probabilité de churn: {prob2*100:.1f}%")
    print(f"  Niveau de risque: {risk2}")