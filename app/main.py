
from fastapi import FastAPI
from app.database import get_db
from app.schemas import ismaeilCreate, ismaeilResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import ismaeil
import joblib
import pandas as pd


app = FastAPI(
    title="Cardio Risk API",
    description="API de prédiction du risque cardiovasculaire",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de risque cardiovasculaire"}

@app.get('/patients',response_model=list[ismaeilResponse])
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(ismaeil).all()
    return patients

# @app.post('/predict',response_model=ismaeilCreate)
# def post_predict(patient_data: ismaeilCreate, db: Session = Depends(get_db)):
#     patient=ismaeil(**patient_data.dict())
#     db.add (patient)
#     db.commit()
#     db.refresh(patient)
#     return patient

model=joblib.load("./ml_pipeline/model_lhcen.pkl")

@app.post("/predict", response_model=ismaeilCreate)
def predict(data: ismaeilCreate, db: Session = Depends(get_db)):
    
    features = pd.DataFrame([{
        "age": data.age,
        "gender": data.gender,
        "pressurehight": data.pressurehight,
        "pressurelow": data.pressurelow,
        "glucose": data.glucose,
        "kcm": data.kcm,
        "troponin": data.troponin,
        "impluse": data.impulse 
    }])
    
    status = int(model.predict(features)[0])


    db_item = ismaeil(
        age=data.age,
        gender=data.gender,
        pressurehight=data.pressurehight,
        pressurelow=data.pressurelow,
        glucose=data.glucose,
        kcm=data.kcm,
        troponin=data.troponin,
        impulse=data.impulse,
        status=status
    )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item