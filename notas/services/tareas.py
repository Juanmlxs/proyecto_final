from schemas.tareas import Tarea
from models.tareas import Tarea as TareaModel

class TareaService():
    def __init__(self, db):
        self.db = db
        
    def get_tareas(self):
        tareas = self.db.query(TareaModel).all()
        return tareas
    
    def get_tarea(self, id: int):
        tarea = self.db.query(TareaModel).filter(TareaModel.id == id).first()
        return tarea
    
    def create_tarea(self, tarea: Tarea):
        new_tarea = TareaModel(**tarea.model_dump())
        self.db.add(new_tarea)
        self.db.commit()
    
    def update_tarea(self, tarea: TareaModel, data:Tarea):
        tarea.tarea = data.tarea
        tarea.descripcion = data.descripcion
        tarea.estado = data.estado
        self.db.commit()
        
    def delete_tarea(self, tarea: TareaModel):
        self.db.delete(tarea)
        self.db.commit()