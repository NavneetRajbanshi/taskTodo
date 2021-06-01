from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def check_password(password, hash_password) -> str:
    return pwd_context.verify(password, hash_password)


def read_user(db: Session, username):
    return db.query(models.Login).filter(models.Login.username == username).first()


def create_user(db: Session, create: schemas.CreateUser):
    hashed_password = get_password_hash(create.password)
    db_user = models.Login(
        first_name=create.first_name,
        last_name=create.last_name,
        username=create.username,
        email=create.email,
        password=hashed_password,
        status=create.status,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def pass_user(db: Session, username):
    user_value = (
        db.query(models.Login).filter(models.Login.username == username).first()
    )
    user_dict = jsonable_encoder(user_value)
    current_user = schema.User(**user_dict)
    return current_user