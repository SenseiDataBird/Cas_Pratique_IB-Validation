# ImmoBird – Prédiction de prix immobilier

---

## Objectif du projet ImmoBird
Développer et valider un module de **prédiction de prix de biens immobiliers** basé sur un jeu de données internes (surface, localisation, état, année de construction, etc.).  
Ce module a vocation à être intégré dans la plateforme **ImmoBird** afin de fournir aux utilisateurs une **estimation instantanée** de leur bien lors de la création d’annonce.

---


---

## Jeu de données

- Fichier : `data_for_model/house_pred_raw.csv`  
- Taille : ~1000 lignes, 6 colonnes  
- Variables disponibles :  
  - `Area` → surface du bien (m²)  
  - `YearBuilt` → année de construction  
  - `Location` → ville (Paris, Lyon, Lille, Marseille)  
  - `Condition` → état général (Excellent, Good, Fair, Poor)  
  - `Garage` → présence d’un garage (Yes/No)  
  - `Price` → prix du bien (target, en €)
 
Fichier : `data_for_model/house_pred_for_ml.csv`
Fichier pré-processé pour Machine Learning

---

## Méthodologie

1. **Prétraitement des données**
   - Gestion des valeurs manquantes
   - Encodage des variables catégorielles
   - Split train/test (80%/20%)  

2. **Modélisation**
   - Baseline : Modèle par médiane des prix (modèle naïf)
   - Incrément+1 : Régression linéaire (explicabilité, interprétabilité)
   - Incrément+2 : XGBoost (meilleures performances)

3. **Évaluation**
   - Métriques :  
     - **RMSE** (Root Mean Squared Error)  
   - Seuil métier attendu : ±10% d’erreur de prédiction moyenne acceptable

---

## Résultats (exemple)

| Modèle              | RMSE (€) | Commentaire                       |
|----------------------|----------|-----------------------------------|
| Régression Linéaire | 107,200  | Incrément+1 simple et explicable     |
| XGBoost             | 31,800   | Incrément+2 Amélioration notable, plus robuste|
