# Cas_Pratique_IB-Validation
### Ce dépôt contient le matériel du cas pratique “Validation”. 
--- 
#### Votre rôle : valider la partie technique du projet ImmoBird en tant que Chef de Projet Data&amp;IA.
---
#### Votre mission : valider l’avancement technique d’un module de prédiction de prix immobilier.
---

## Le repo contient :

- **1_script_to_validate/model_training_to_validate.py** → version initiale (contient des red flags).

- **2_script_cleaned/model_training_cleaned.py** → version corrigée par un Data Scientist.

- **data_for_model/house_pred_for_ml.csv → jeu de données** (vous n’avez pas à l’ouvrir ni à l’exécuter).

### Aucun prérequis technique requis. 
#### *Ne lancez pas le code : votre rôle est de lire et décider.*
---

## Objectifs :

- **Savoir repérer** les red flags (sécurité, reproductibilité, qualité, traçabilité).

- **Savoir formuler des recommandations claires** et décider Go/No-Go.

### **Étape 1 — Valider le script initial**

**Fichier à lire :**
>1_script_to_validate/model_training_to_validate.py

**Ce que vous devez repérer (en 5 points ou plus si compétences techniques) :**

- Secrets / identifiants en clair (ex. URL avec mot de passe).

- Chemins absolus (ex. C:\Users\...) au lieu de chemins relatifs.

- Logging : pas de traçabilité.

- Reproductibilité : absence de random_state (split/modèles).

- Métriques absentes (ex. pas de RMSE affiché).

### **Livrable étape 1 :**
>Ouvrez 1_script_to_validate/checklist_CDP.md et remplissez :

- OK/KO pour chaque point.

- 1 phrase de justification par point KO.

- **Décision : Go ou demande de modification.**

- (Optionnel) : 3 recommandations concrètes.

- **Risque principal (1 phrase).**

---
### *Suite à lire une fois l'étape 1 terminée de votre côté*
---

## Résultat (scénario) :

*Suite à votre revue, un Data Scientist applique vos demandes et livre une version propre du script.*

### **Étape 2 — Valider le script corrigé**

**Fichier à lire :**
>2_script_cleaned/model_training_cleaned.py

** Il ne vous reste plus qu'à valider le traitement de votre demande !**

**Livrable étape 2 :**
>Ouvrez 2_script_cleaned/checklist_CDP_new.md et complétez.


**Astuce pour compléter vos livrables :**

*Dans le repo Git, cliquez sur le fichier → (edit) → remplissez → Commit changes.*
