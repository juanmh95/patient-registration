from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from app.config import get_settings

config = get_settings()

DATABASE_URL = config.get_database_url()

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

def init_db():
    from app.models.patient import PatientModel 
    Base.metadata.create_all(bind=engine)