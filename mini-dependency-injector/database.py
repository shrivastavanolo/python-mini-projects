from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./test.db")
SessionLocal = sessionmaker(bind=engine)
