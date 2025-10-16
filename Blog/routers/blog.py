from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from grpc import Status
from Blog import models, schemas
from Blog.database import get_db
from sqlalchemy.orm import Session

router=APIRouter()


@router.get('/blog',response_model=List[schemas.ShowBlog],tags=["Blogs"])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blogss',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
def creating_post(request:schemas.Blog,db: Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/blogs/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} id not found")
    blog.update(request.model_dump())
    db.commit()
    return f" Update Data of id: {id}"





@router.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=["Blogs"])
def specific(id,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    return blogs


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def deletes(id,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id )
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    blog.delete(synchronize_session=False)
    db.commit()
    return f"It {id} delete "

@router.post('/blogss',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
def creating_post(request:schemas.Blog,db: Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/blogs/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} id not found")
    blog.update(request.model_dump())
    db.commit()
    return f" Update Data of id: {id}"


@router.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=["Blogs"])
def specific(id,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    return blogs


@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def deletes(id,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id )
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    blog.delete(synchronize_session=False)
    db.commit()
    return f"It {id} delete "
