from sqlalchemy.orm import Session
from .models import Users


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Users).offset(skip).limit(limit).all()