from pydantic import BaseModel
from typing import Optional

# Modelo principal de Iris
class Iris(BaseModel):
    id: Optional[int] = None
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: Optional[str] = None
    classifier: Optional[str] = None

# Modelo para recibir unicamente el ID de la fila a eliminar
class IrisDelete(BaseModel):
    id: int