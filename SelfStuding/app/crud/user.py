from sqlalchemy.orm import Session
from ..models import user
from ..schemas import user as user_schemas
from ..core.security import hash_password

def create_user(db: Session, user_data: user_schemas.UserCreate):
    db_user = user.User(username=user_data.username, email=user_data.email, password_hash=hash_password(user_data.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user