# 🏦 Bank Churn Prediction

Application web de prédiction du risque de départ (churn) des clients bancaires utilisant le Machine Learning.


## 🎯 Objectif

Prédire la probabilité qu'un client quitte la banque en utilisant un modèle XGBoost entraîné sur 10,000 clients historiques.

## 🚀 Demo Live

**[Tester l'application en ligne](https://bank-churn-prediction-ibrahym00.streamlit.app/)**

## 📊 Fonctionnalités

- **Prédiction en temps réel** : Saisie des informations client et prédiction instantanée
- **Niveau de risque** : Classification Faible/Moyen/Élevé avec probabilité
- **Recommandations business** : Suggestions d'actions personnalisées
- **Analytics** : Visualisation de l'importance des variables
- **Interface intuitive** : Application web responsive et professionnelle

## 🧠 Modèle

- **Algorithme** : XGBoost (Gradient Boosting)
- **Performance** : ROC-AUC de 0.857
- **Recall** : 62% (détecte 62% des clients à risque)
- **Accuracy** : 83.7%

## 📈 Insights Clés

- Les clients **allemands** ont 2x plus de risque (32% vs 16%)
- Les **femmes** partent plus que les hommes (25% vs 16%)
- Les **50-60 ans** ont un risque très élevé (56%)
- Les **membres inactifs** ont 2x plus de risque (27% vs 14%)
- **2 produits** = sweet spot (7.6% de churn vs 27.7% avec 1 produit)

## 🛠️ Technologies Utilisées

- **Python 3.11**
- **Streamlit** : Interface web
- **XGBoost** : Modèle de Machine Learning
- **Pandas & NumPy** : Manipulation de données
- **Plotly** : Visualisations interactives
- **Scikit-learn** : Preprocessing et métriques
- **SMOTE** : Équilibrage des classes

## 📂 Structure du Projet
```
bank-churn-prediction/
├── app/
│   └── streamlit_app.py      # Application Streamlit
├── data/
│   ├── raw/                   # Données brutes
│   └── processed/             # Données préparées
├── models/
│   ├── xgboost_churn_model.pkl  # Modèle entraîné
│   └── model_info.pkl         # Métadonnées
├── notebooks/
│   ├── 01_exploration.ipynb   # EDA
│   └── 02_preprocessing_modeling.ipynb  # Modélisation
├── src/
│   ├── download_data.py       # Téléchargement données
│   └── predict.py             # Script de prédiction
├
│   
├── requirements.txt           # Dépendances
└── README.md
```

## 🚀 Installation et Utilisation

### Prérequis

- Python 3.8+
- pip

### Installation

1. Cloner le repository
```bash
git clone https://github.com/TON_USERNAME/bank-churn-prediction.git
cd bank-churn-prediction
```

2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Lancer l'application
```bash
cd app
streamlit run streamlit_app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à `http://localhost:8501`

## 📊 Données

- **Source** : Dataset de 10,000 clients bancaires
- **Variables** : 12 features (âge, solde, pays, nombre de produits, etc.)
- **Cible** : Churn (0 = reste, 1 = part)
- **Taux de churn** : 20.37%

##  Méthodologie

1. **Exploration des données (EDA)**
   - Analyse univariée et bivariée
   - Identification des segments à risque
   - Visualisations

2. **Preprocessing**
   - Encodage des variables catégorielles
   - Split Train/Test (80/20)
   - Application de SMOTE (équilibrage)

3. **Modélisation**
   - Comparaison de 3 algorithmes (Logistic, Random Forest, XGBoost)
   - Sélection de XGBoost (meilleur ROC-AUC)
   - Sauvegarde du modèle

4. **Déploiement**
   - Application Streamlit
   - Déploiement sur Streamlit Cloud

## ⚠️ Limitations

- Modèle entraîné uniquement sur **France, Germany, Spain**
- Basé sur des données historiques (peut nécessiter une mise à jour)
- Ne prend pas en compte les données temporelles ou saisonnières

## 📈 Améliorations Futures

- [ ] Ajouter un mode batch (upload CSV)
- [ ] Intégrer des données temporelles
- [ ] Déployer une API REST
- [ ] A/B testing des recommandations
- [ ] Tableau de bord de suivi des prédictions

##  Auteur

**Ibrahim DABRE**


##  Licence

Tous droits réservés © 2025 Ibrahim DABRE

---

⭐ Si ce projet vous a plu, n'hésitez pas à mettre une étoile !
