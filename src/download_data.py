"""
Script pour télécharger les données de churn bancaire
"""

import pandas as pd
import os

def download_bank_churn_data():
    """
    Télécharge le dataset Bank Churn depuis GitHub
    
    Return:
        DataFrame pandas avec les données
    """
    
    url = "https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Bank%20Churn%20Modelling.csv"
    output_path = "data/raw/bank_churn.csv"
    
    print("Téléchargement des données...")
    
    try:
        # Lecture du CSV depuis l'URL
        df = pd.read_csv(url)
        
        # Sauvegarde locale
        df.to_csv(output_path, index=False)
        
        print(f"Données téléchargées: {len(df)} lignes, {len(df.columns)} colonnes")
        print(f"Sauvegardées dans: {output_path}")
        
        print("\nAperçu des données:")
        print(df.head())
        
        print("\nColonnes disponibles:")
        print(df.columns.tolist())
        
        return df
        
    except Exception as e:
        print(f"Erreur: {e}")
        return None

if __name__ == "__main__":
    data = download_bank_churn_data()