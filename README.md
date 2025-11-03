<div align="center">
  <br />
  <img src="https://www.simplon.ma/images/Simplon_Maghreb_Rouge.png" alt="Simplon Maghreb Logo" width="300"/>
  <br /><br />

  <div>
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python&logoColor=white&color=3776AB" />
    <img src="https://img.shields.io/badge/-FastAPI-black?style=for-the-badge&logo=fastapi&logoColor=white&color=009688" />
    <img src="https://img.shields.io/badge/-SQLite-black?style=for-the-badge&logo=sqlite&logoColor=white&color=003B57" />
    <img src="https://img.shields.io/badge/-Scikit--Learn-black?style=for-the-badge&logo=scikitlearn&logoColor=white&color=F7931E" />
    <img src="https://img.shields.io/badge/-SQLAlchemy-black?style=for-the-badge&logo=python&logoColor=white&color=E34F26" />
    <img src="https://img.shields.io/badge/-Pytest-black?style=for-the-badge&logo=pytest&logoColor=white&color=0A9EDC" />
  </div>

  <h1>🩺 API de Machine Learning Santé – Prédiction de Risque</h1>
  <p><strong>Projet IA</strong> – Simplon Maghreb</p>
</div>

---

## 🧩 Introduction

Cette API permet de predire le risque medical d’un patient a partir de ses donnees cliniques en utilisant un modele de Machine Learning.  
Elle est developpee avec **FastAPI**, offrant une documentation interactive **Swagger UI**.

---

## 🎯 Objectif du projet

L’objectif est de concevoir une API REST capable de :

- Charger un modele d’apprentissage automatique (ex. RandomForestClassifier, SVR.)
- Recevoir des données patient sous forme JSON
- Retourner la probabilite de risque predite par le modele
- Fournir une documentation interactive Swagger pour tester facilement les endpoints.

---

## 📥 Exemple de requête

```json
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
📤 Exemple de réponse
json
Copy code
{
  "age": 55,
  "gender": 1,
  "pressurehight": 140,
  "pressurelow": 90,
  "glucose": 110,
  "kcm": 5.5,
  "troponin": 0.03,
  "impulse": 80,
  "status": 1
}
<div align="center"> <p>👨‍💻 Projet réalisé par <strong><a href="https://github.com/OclaZ">OclaZ</a></strong> | Simplon Maghreb</p> </div> ```
