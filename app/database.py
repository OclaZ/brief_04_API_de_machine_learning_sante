# Import necessary modules and classes
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite:///./hamza.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ismaeil(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    gender = Column(Integer)
    pressurehight= Column(Integer)
    pressurelow = Column(Integer)
    glucose = Column(Integer)
    kcm= Column(Float)
    troponin= Column(Float)
    impulse= Column(Float)
    status= Column(Integer)


Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()