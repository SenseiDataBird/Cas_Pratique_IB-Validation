# Checklist de validation CDP – Cas pratique ImmoBird

---

## 1. Documentation & compréhension
- [ ] Le **README_immobird** permet de comprendre rapidement le projet (objectif, données, modèle, exécution).  
- [ ] Chaque fichier du repo a une **utilité claire** (donnée, code, config, doc).  
- [ ] Les dépendances sont listées dans `requirements.txt` (versions figées de préférence).  

---

## 2. Sécurité & conformité
- [ ] Aucun **secret/identifiant en clair** (mot de passe, clé API, chemin privé).  
- [ ] Pas de **chemins absolus** (`C:\Users\...` ou `/home/...`) → uniquement des chemins relatifs.  
- [ ] Les fichiers sensibles ou lourds sont **exclus du repo** via `.gitignore` (ex. data brutes, .env).  

---

## 3. Qualité & traçabilité
- [ ] Le script inclut un **logging minimal** (erreurs, étapes clés, résultats).  
- [ ] Le code est **lisible et commenté** (variables claires, pas de lignes inutiles).  
- [ ] La logique métier est **séparée** (ex. données ≠ modèle ≠ résultats).  

---

## 4. Reproductibilité
- [ ] Le split train/test et les modèles utilisent un **`random_state` fixé**.  
- [ ] Le pipeline peut être **rejoué à l’identique** par un autre membre de l’équipe.  
- [ ] Les librairies utilisées sont stables et cohérentes (pas de dépendances inutiles).  

---

## 5. Métriques & validation
- [ ] Au moins une **métrique de performance** est calculée et affichée (ex. RMSE, R², Accuracy).  
- [ ] La métrique est **alignée avec le besoin métier** (ex. ±10% sur le prix = cohérent avec NSM).  
- [ ] Un **baseline simple** (modèle de référence) est présent pour comparer.  

---

## 6. Décision CDP
- **Points KO identifiés :**  
  - …  
- **Recommandations prioritaires :**  
  - …  
- **Décision :**  
  - [ ] Go (script validé pour la suite)  
  - [ ] No-Go (changements nécessaires avant livraison)  
