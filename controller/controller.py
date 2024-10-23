from fastapi import APIRouter, HTTPException
from typing import List, Dict
from model.models import Equipo, Jugador
from service.service import LigaService

router = APIRouter()
liga_service = LigaService()

@router.get("/equipos/", response_model=List[Equipo])
async def listar_equipos():
    return liga_service.obtener_equipos()

@router.get("/equipo/{nombre}/promedio-edad")
async def obtener_promedio_edad(nombre: str):
    promedio = liga_service.obtener_promedio_edad(nombre)
    return {"equipo": nombre, "promedio_edad": promedio}

@router.get("/equipo/{nombre}/goleador", response_model=Jugador)
async def obtener_goleador(nombre: str):
    goleador = liga_service.obtener_goleador(nombre)
    return goleador

@router.get("/equipo/{nombre}/jugadores/{posicion}")
async def filtrar_jugadores_por_posicion(nombre: str, posicion: str):
    jugadores = liga_service.filtrar_por_posicion(nombre, posicion)
    return jugadores
