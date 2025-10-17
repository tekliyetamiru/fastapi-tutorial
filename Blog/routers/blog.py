from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from grpc import Status
from Blog import models, schemas
from Blog.database import get_db
from sqlalchemy.orm import Session

from Blog.repository import blog
from Blog.routers.Oauth2 import get_current_user

router=APIRouter(
     prefix='/blog'
    ,tags=["Blogs"]

)


@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def creating_post(request:schemas.Blog,db: Session = Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.create(request,db)
    

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
   return blog.update(request,db)


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def specific(id:int,db:Session = Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
   return blog.specific(id,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletes(id,db:Session = Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.id == id )
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    blog.delete(synchronize_session=False)
    db.commit()
    return f"It {id} delete "

@router.post('/',status_code=status.HTTP_201_CREATED)
def creating_post(request:schemas.Blog,db: Session = Depends(get_db),current_user:schemas.User=Depends(get_current_user)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} id not found")
    blog.update(request.model_dump())
    db.commit()
    return f" Update Data of id: {id}"


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def specific(id,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    return blogs


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletes(id,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id )
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    blog.delete(synchronize_session=False)
    db.commit()
    return f"It {id} delete "
