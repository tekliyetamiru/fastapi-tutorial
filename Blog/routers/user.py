from fastapi import APIRouter, Depends, HTTPException, status

from Blog import models, schemas
from Blog.database import get_db
from Blog.hashing import Hash

from sqlalchemy.orm import Session

router=APIRouter()










@router.post('/user',response_model=schemas.ShowUser,tags=["Users"])
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/bloguser',tags=["Users"])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.User).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User is not available") 
    return blogs

@router.get('/user/{id}',tags=["Users"])
def getuser(id,db:Session = Depends(get_db)):
    userbyid=db.query(models.User).filter(models.User.id ==id).first()
    if not userbyid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not found or availble") 
    return userbyid
