from fastapi import Depends, FastAPI, HTTPException,status
from sqlalchemy.orm import Session
import uvicorn
from Blog.database import SessionLocal, engine
from Blog import models, schemas


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/blogss',status_code=status.HTTP_201_CREATED)
def creating_post(request:schemas.Blog,db: Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blogs/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id: {id} id not found")
    blog.update(request.model_dump())
    db.commit()
    return f" Update Data of id: {id}"



@app.get('/blog')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
def specific(id,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    return blogs

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletes(id,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id )
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found or availble") 
    blog.delete(synchronize_session=False)
    db.commit()
    return f"It {id} delete "

@app.post('/user')
def create_user(request:schemas.User):
    return request