# =======================================================================================================================================
# ImmoBird - Model Training
# Baseline → Linéaire → XGBoost
# ---------------------------------------------------------------------------------------------------------------------------------------
# Sans red flags, propre
# =======================================================================================================================================

# Importations packages de logging
import logging

# Importations packages de preprocessing
import pandas as pd
import numpy as np

from math import sqrt

from pathlib import Path

# Importations packages de modélisation
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from xgboost import XGBRegressor

# 0. Configuration de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 1. Charger les données de manière robuste
data_path = Path("data_for_model/house_pred_for_ml.csv")
if not data_path.exists():
    raise FileNotFoundError(f"Fichier introuvable : {data_path}")

df = pd.read_csv(data_path)
logger.info("Dataset chargé : %s (%d lignes, %d colonnes)", data_path, df.shape[0], df.shape[1])

if "Price" not in df.columns:
    raise ValueError("La colonne cible 'Price' est manquante dans le dataset")

X = df.drop("Price", axis=1)
y = df["Price"]

# Vérification qualité minimale
if X.isnull().sum().any():
    print("Données manquantes détectées. Vérifiez le preprocessing.")

# 2. Détection automatique des variables
num_cols = [c for c in X.columns if pd.api.types.is_numeric_dtype(X[c])]
cat_cols = [c for c in X.columns if not pd.api.types.is_numeric_dtype(X[c])]

# Split reproductible
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Baseline simple
def baseline_predict(X_train, y_train, X_test):
    """Baseline : médiane par ville si dispo, sinon médiane globale"""
    global_median = y_train.median()
    if "Location" in X_train.columns:
        train_data = pd.concat([X_train["Location"], y_train], axis=1)
        med_by_loc = train_data.groupby("Location")["Price"].median().to_dict()
        return X_test["Location"].map(med_by_loc).fillna(global_median)
    return pd.Series([global_median] * len(X_test))

y_pred_base = baseline_predict(X_train, y_train, X_test)
rmse_base = sqrt(mean_squared_error(y_test, y_pred_base))
logger.info("Baseline RMSE: %.0f", rmse_base)

# 4. Pipeline régression linéaire
preprocess = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

linreg_model = Pipeline([
    ("preprocess", preprocess),
    ("regressor", LinearRegression())
])

linreg_model.fit(X_train, y_train)
y_pred_lin = linreg_model.predict(X_test)
rmse_lin = sqrt(mean_squared_error(y_test, y_pred_lin))
logger.info("Linear Regression RMSE: %.0f", rmse_lin)

# 5. Pipeline XGBoost
xgb_model = Pipeline([
    ("preprocess", preprocess),
    ("regressor", XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42,
        n_jobs=-1
    ))
])

xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)
rmse_xgb = sqrt(mean_squared_error(y_test, y_pred_xgb))
logger.info("XGBoost RMSE: %.0f", rmse_xgb)
