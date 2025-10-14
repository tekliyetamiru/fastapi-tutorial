


from pydantic import BaseModel, ConfigDict


class Blog(BaseModel):
    title:str
    body:str


class ShowBlog(BaseModel):
    title:str
    id:int
    model_config = ConfigDict(from_attributes=True)

class User(BaseModel):
    name:str
    email:str
    password:str

