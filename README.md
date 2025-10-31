# API de Machine Learning Santé – Prédiction de Risque

Cette API permet de predire le risque medical d’un patient a partir de ses donnees cliniques en utilisant un modele de Machine Learning.  
Elle est developpee avec FastAPI, offrant une documentation interactive Swagger UI.

## Objectif du projet
L’objectif est de concevoir une API REST capable de :
- Charger un modele d’apprentissage automatique (ex. RandomForestClassifier, SVR.)
- Recevoir des données patient sous forme JSON
- Retourner la probabilite de risque predite par le modele  
- Fournir une documentation interactive Swagger pour tester facilement les endpoints:
exemple :
```
{
      "age": 55,
        "gender": 1,
        "pressurehight": 140,
        "pressurelow": 90,
        "glucose": 110,
        "kcm": 5.5,
        "troponin": 0.03,
        "impulse": 80
}
```
exemple de reponse :
```
{
        age": 55,
        "gender": 1,
        "pressurehight": 140,
        "pressurelow": 90,
        "glucose": 110,
        "kcm": 5.5,
        "troponin": 0.03,
        "impulse": 80
        "status" : 1  !!!
}
```
