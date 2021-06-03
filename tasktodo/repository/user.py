from sqlalchemy.orm import Session
from tasktodo import models, schemas
from fastapi import HTTPException,status
from tasktodo.hashing import Hash

def create(request: schemas.User ,db:Session):
    new_user = models.User(first_name=request.first_name,last_name=request.last_name,user_name=request.user_name,
    email=request.email,status=request.status, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    User = db.query(models.User).filter(models.User.id == id).first()
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return User