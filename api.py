from fastapi import FastAPI
from todo import todo
app = FastAPI()
@app.get("/")

def home():
    return "Bienvenidos"

@app.get("/name/{name}")#son enlaces del servidor web
def greeting(name:str):
    return "hello "+name

app.include_router(todo)