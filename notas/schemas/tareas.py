from pydantic import BaseModel, Field
from typing import Optional

class Tarea(BaseModel):
    id: Optional[int] = None
    tarea: str = Field(default="Hacer tarea", min_length=1, max_length=100)
    descripcion: str = Field(default="Hacer la tarea de matematicas", min_length=1, max_length=500)
    estado: str = Field(default="pendiente", min_length=1, max_length=12)
    
    # Configuracion de la documentacion

    class Config:
        moldel_config = {
            'json_squema_extra': {
                "example": [
                    {
                        "tarea": "Hacer tarea",
                        "descripcion": "Hacer la tarea de matematicas",
                        "estado": "pendiente",
                        "id": 1
                    }
                ]
            }
        } 