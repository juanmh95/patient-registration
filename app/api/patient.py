from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.database.curd import create_patient as curd_create_patient, get_all_patients
from app.models.patient import PatientCreate
from app.database.database import SessionLocal
from app.tasks.email import send_mail

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/patients/")
async def create_patient(patient: PatientCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # Database operation
    patient_created = await curd_create_patient(db, patient)
    sender = "Private Person <from@example.com>"
    receiver = f"{patient_created.name} <{patient_created.email}>"
    message = f"""\
        Subject: Hi Mailtrap
        To: {receiver}
        From: {sender}

        Patient {patient_created.name} has been registred."""
    background_tasks.add_task(send_mail, sender, receiver, message)
    return {'created': patient_created}

@router.get("/patients/")
async def get_all(db: Session = Depends(get_db)):
    return {"patients":await get_all_patients(db)}