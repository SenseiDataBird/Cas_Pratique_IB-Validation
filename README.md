# Cas_Pratique_IB-Validation  
### Ce dépôt contient le matériel du cas pratique **“Validation”**.  

---

#### Votre rôle : **valider la partie technique du projet ImmoBird en tant que Chef de Projet Data & IA.**  

---

#### Votre mission : analyser et **valider l’avancement technique** d’un module de prédiction de prix immobilier.  

---

## Le repo contient :  

- **1_script_to_validate/model_training_to_validate.py** → version initiale (contient des erreurs / red flags).  
- **2_script_cleaned/model_training_cleaned.py** → version corrigée + rajout d'un 2ème incrément par un Data Scientist + Un fichier **README_immobird.md** qui documente le projet.  
- **data_for_model/house_pred_for_ml.csv** : données source / **data_for_model/house_pred_for_ml.csv** : données transformées pour ML → jeux de données (**vous n’avez pas à l’ouvrir ni à l’exécuter**).  

---

### Aucun prérequis technique requis.  
*Ne lancez pas le code : votre rôle est de lire, comprendre (avec Cursor) et décider.*  

---

## Objectifs :  

- **Utiliser Cursor pour comprendre** la structure du repo et le rôle des fichiers.  
- **Repérer les red flags** (sécurité, reproductibilité, qualité, traçabilité) → Référez-vous au cours "savoir lire Python" (jour 1, module 2).  
- **Formuler des recommandations claires** et décider.  

---

## Étape 1 — Valider le script initial  

**Fichier à lire :**  
`1_script_to_validate/model_training_to_validate.py`  

**Ce que vous devez repérer (au moins 5 points) :**  
- Secrets / identifiants en clair.  
- Chemins absolus (ex. `C:\Users\...`) au lieu de chemins relatifs.  
- Pas de reproductibilité (absence de `random_state` dans split/modèles).  
- Métriques absentes (ex. pas de RMSE affiché, pas de métrique de performance du modèle).  

**Livrable étape 1 (avec Cursor) :**  
- Compléter la **checklist de validation** dans le fichier `1_script_to_validate` avec :  
  - OK/KO pour chaque point.  
  - 1 phrase de justification par point KO.  
  - (Optionnel) : 3 recommandations concrètes.
    
---

## Résultat (scénario du cas pratique pour la deuxième partie) :  

Suite à vos remarques, le Data Scientist applique vos demandes et livre une version propre du script.  

---

## Étape 2 — Valider le script corrigé  

**Fichier à lire :**  
`2_script_cleaned/model_training_cleaned.py`  

**Livrable étape 2 (avec Cursor) :**  
- Relisez le script corrigé.  
- Vérifiez que vos demandes ont bien été prises en compte.  
- Décidez si le script est **validé pour prochaine étape du workflow en fonction de votre checklist**.  
