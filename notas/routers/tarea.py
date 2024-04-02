from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Path, Query, Depends

from schemas.tareas import Tarea
from config.database import Session
from services.tareas import TareaService
from models.tareas import Tarea as TareaModel


tarea_router = APIRouter()

@tarea_router.get("/tareas", tags=['Tareas'],response_model=List[Tarea], status_code=202)
def get_tareas() -> List[Tarea]:
    db_session = Session()
    tareas = TareaService(db_session).get_tareas()
    return JSONResponse(content=jsonable_encoder(tareas), status_code=202)

@tarea_router.get("/tarea/{id}", tags=['Tareas'], response_model=Tarea, status_code=202)
def get_tarea(id) -> Tarea:
    db_session = Session()
    tarea = TareaService(db_session).get_tarea(id)
    return JSONResponse(content=jsonable_encoder(tarea), status_code=202)

@tarea_router.post("/tareas", tags=['Tareas'], status_code=201, response_model=dict)
def create_tarea(tarea: Tarea) -> Tarea:
    db_session = Session() 
    TareaService(db_session).create_tarea(tarea)
    return JSONResponse(content={"message": "Tarea updated successfully"}, status_code=201)

@tarea_router.put("/tareas/{id}", tags=['Tareas'], status_code=202, response_model=dict)
def update_tarea(id: int, tarea: Tarea) -> dict:
    db_session = Session()
    tarea_db = TareaService(db_session).get_tarea(id)
    if not tarea_db:
        response = JSONResponse(content={"message": "Tarea not found"}, status_code=404)
    else:
        TareaService(db_session).update_tarea(tarea_db, tarea)
        response = JSONResponse(content={"message": "Tarea updated successfully"}, status_code=202)
    return response

@tarea_router.delete("/tareas/{id}", tags=['Tareas'], status_code=202, response_model=dict)
def delete_tarea(id: int) -> dict:
    db_session = Session()
    tarea = TareaService(db_session).get_tarea(id)
    if not tarea:
        response = JSONResponse(content={"message": "Tarea not found"}, status_code=404)
    else:
        TareaService(db_session).delete_tarea(tarea)
        response = JSONResponse(content={"message": "Tarea deleted successfully"}, status_code=202)
    return response