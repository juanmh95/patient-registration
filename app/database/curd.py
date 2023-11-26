from sqlalchemy.orm import Session
from app.models.patient import PatientModel, PatientCreate

async def create_patient(db: Session, patient: PatientCreate):
    db_patient = PatientModel(name=patient.name, email=patient.email, phone=patient.phone, doc_photo=patient.doc_photo)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

async def get_all_patients(db: Session):
    patients = db.query(PatientModel).all()
    return patients