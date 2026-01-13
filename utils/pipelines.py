from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from xgboost import XGBClassifier

from sklearn.feature_selection import (
    SelectKBest,
    f_classif
)

scaler = StandardScaler()

selector = SelectKBest(score_func=f_classif, k='all')

models_pipelines = {
    'RandomForest_Pipeline': Pipeline([
    ('scaler', scaler),
    ('selection', selector),
    ('model', RandomForestClassifier(random_state=42, n_jobs=-1))
]),
    'KNN_Pipeline': Pipeline([
    ('scaler', scaler),
    ('selection', selector),
    ('model', KNeighborsClassifier(n_jobs=-1))
]),
    'XGBoost_Pipeline': Pipeline([
    ('scaler', scaler),
    ('selection', selector),
    ('model', XGBClassifier(
        use_label_encoder=False,
        eval_metric='mlogloss',
        random_state=42,
        n_jobs=-1
    ))
]),
    'QDA_Pipeline': Pipeline([
    ('scaler', scaler),
    ('selection', selector),
    ('model', QuadraticDiscriminantAnalysis())

])}
