# =======================================================================================================================================
# ImmoBird - Model Training
# Baseline → Linéaire → XGBoost
# ---------------------------------------------------------------------------------------------------------------------------------------
# Avec red flags à détecter
# =======================================================================================================================================

# Importations des packages de traitement de la donnée
import pandas as pd
import numpy as np 

# Importation des packages de modélisation de la donnée
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

# --- 1) Chargement des données - détecter le red flag :
df = pd.read_csv("C:/Users/erwan/Desktop/house_pred_for_ml.csv")

# --- 1.1) Phase manquante très importante à détecter :
# ...

# --- 1.2) Phase manquante très importante à détecter :
# ...

X = df.drop("Price", axis=1)
y = df["Price"]

# --- 2) Split train/test - détecter le red flag :
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# --- 3) Baseline - détecter le red flag :
def baseline_predict(X_train, y_train, X_test):

    global_median = y_train.median()

    if "Location" in X_train.columns:
        train_data = pd.concat([X_train["Location"], y_train], axis=1)
        med_by_loc = train_data.groupby("Location")["Price"].median().to_dict()

        return X_test["Location"].map(med_by_loc).fillna(global_median)

    return pd.Series([global_median] * len(X_test))

y_pred_base = baseline_predict(X_train, y_train, X_test)

# --- 3.1) Modèle entraîné - détecter le red flag :
print("Baseline entraînée (aucune métrique affichée).")

# --- 4) Régression linéaire
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred_lin = linreg.predict(X_test)

# --- 4.1) Modèle entraîné - détecter le red flag (le même qu'en 3.1)):
print("Régression linéaire entraînée (aucune métrique affichée).")