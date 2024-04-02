from config.database import Base
from sqlalchemy import Column, Integer, String

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    tarea = Column(String)
    descripcion = Column(String)
    estado = Column(String)
