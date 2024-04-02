from fastapi.responses import HTMLResponse
from fastapi import FastAPI

from config.database import engine, Base
from routers.tarea import tarea_router


app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(tarea_router)
app.title = "La super API" 
app.version = "2.0.0"

@app.get("/", tags=['home'])
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")