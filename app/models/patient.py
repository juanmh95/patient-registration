from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import BINARY, Column, Integer, String

from app.database.database import Base

class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    doc_photo: str
    # doc_photo: bytes


class PatientModel(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)
    email = Column(String(100), index=True)
    phone = Column(String(100))
    doc_photo = Column(String(100))
    # doc_photo = Column(BINARY)