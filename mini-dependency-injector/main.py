from database import SessionLocal
from typing import Generator
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/users')
def get_users(db: Session = Depends(get_db)):
    rows = db.execute(text('SELECT 1, 2')).fetchall()
    return {"Users": [tuple(row) for row in rows]}
