from typing import List, Optional
from pydantic import BaseModel

class Persona(BaseModel):
    nombre: str
    apellido: str
    edad: int

class Jugador(Persona):
    posicion: str
    goles: int

class Entrenador(Persona):
    anos_experiencia: int

class Equipo(BaseModel):
    nombre: str
    entrenador: Entrenador
    jugadores: List[Jugador]

class Liga(BaseModel):
    nombre: str
    equipos: List[Equipo] = []
