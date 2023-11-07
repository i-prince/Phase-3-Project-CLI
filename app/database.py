from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Database configuration
DATABASE_URL = "sqlite:///mydatabase.db"

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
