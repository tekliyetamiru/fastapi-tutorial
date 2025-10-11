from fastapi import FastAPI
app = FastAPI()
  




@app.get('/')
def index():
    return {'ab':{"page":"heyy"}}


@app.get('/about')
def aboutpage():
    return  {"data":"page"}