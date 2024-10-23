from typing import List, Optional
from model.models import Jugador, Entrenador, Equipo, Liga


class LigaService:
    def __init__(self):
        self.liga = Liga(nombre="Liga Mundial")
        self._inicializar_equipos()

    def _crear_jugador(self, nombre: str, apellido: str, edad: int, posicion: str, goles: int) -> Jugador:
        return Jugador(nombre=nombre, apellido=apellido, edad=edad, posicion=posicion, goles=goles)

    def _crear_entrenador(self, nombre: str, apellido: str, edad: int, anos_experiencia: int) -> Entrenador:
        return Entrenador(nombre=nombre, apellido=apellido, edad=edad, anos_experiencia=anos_experiencia)

    def _inicializar_equipos(self):

        barcelona_jugadores = [
            self._crear_jugador("Marc", "Ter Stegen", 31, "portero", 0),
            self._crear_jugador("Alejandro", "Balde", 20, "defensa", 2),
            self._crear_jugador("Ronald", "Araujo", 24, "defensa", 2),
            self._crear_jugador("Inigo", "Martinez", 32, "defensa", 2),
            self._crear_jugador("Jules", "Kounde", 25, "defensa", 2),
            self._crear_jugador("Pablo", "Gavi", 19, "mediocampista", 8),
            self._crear_jugador("Pedro", "Gonzalez", 21, "mediocampista", 8),
            self._crear_jugador("Frenkie", "De Jong", 26, "mediocampista", 8),
            self._crear_jugador("Lamine", "Yamal", 16, "delantero", 20),
            self._crear_jugador("Robert", "Lewandowski", 35, "delantero", 20),
            self._crear_jugador("Rafael", "Raphinha", 27, "delantero", 20),
            self._crear_jugador("Iñaki", "Peña", 25, "portero", 0),
        ]

        barcelona = Equipo(
            nombre="Barcelona",
            entrenador=self._crear_entrenador("Hansi", "Flick", 58, 15),
            jugadores=barcelona_jugadores
        )

        self.liga.equipos.append(barcelona)

        realmadrid_jugadores = [
            self._crear_jugador("Thibaut", "Courtois", 32, "portero", 0),
            self._crear_jugador("Eder", "Militao", 26, "defensa", 2),
            self._crear_jugador("Antonio", "Rudiger", 31, "defensa", 2),
            self._crear_jugador("Ferland", "Mendy", 29, "defensa", 2),
            self._crear_jugador("Daniel", "Carvajal", 32, "defensa", 2),
            self._crear_jugador("Federico", "Valverde", 26, "mediocampista", 8),
            self._crear_jugador("Eduardo", "Camavinga", 21, "mediocampista", 8),
            self._crear_jugador("Jude", "Bellingham", 21, "mediocampista", 8),
            self._crear_jugador("Kylian", "Mbappe", 25, "delantero", 30),
            self._crear_jugador("Vinicius", "Junior", 24, "delantero", 20),
            self._crear_jugador("Rodrigo", "Goes", 23, "delantero", 20),
            self._crear_jugador("Andriy", "Lunin", 25, "portero", 0),
        ]

        realmadrid = Equipo(
            nombre="Real Madrid",
            entrenador=self._crear_entrenador("Carlo", "Ancelotti", 65, 20),
            jugadores=realmadrid_jugadores
        )

        self.liga.equipos.append(realmadrid)

        bayernmunchen_jugadores = [
            self._crear_jugador("Manuel", "Neuer", 38, "portero", 0),
            self._crear_jugador("Dayot", "Upamecano", 25, "defensa", 2),
            self._crear_jugador("Kim", "Min-Jae", 27, "defensa", 2),
            self._crear_jugador("Eric", "Dier", 30, "defensa", 2),
            self._crear_jugador("Alphonso", "Davies", 23, "defensa", 2),
            self._crear_jugador("Joshua", "Kimmich", 29, "mediocampista", 8),
            self._crear_jugador("Leon", "Goretzka", 29, "mediocampista", 8),
            self._crear_jugador("Thomas", "Muller", 35, "mediocampista", 8),
            self._crear_jugador("Jamal", "Musiala", 21, "delantero", 15),
            self._crear_jugador("Harry", "Kane", 31, "delantero", 50),
            self._crear_jugador("Michael", "Olise", 22, "delantero", 20),
            self._crear_jugador("Sven", "Ulreich", 36, "portero", 0),
        ]

        bayernmunchen = Equipo(
            nombre="Bayern Munchen",
            entrenador=self._crear_entrenador("Vincent", "Kompany", 38, 4),
            jugadores=bayernmunchen_jugadores
        )

        self.liga.equipos.append(bayernmunchen)

        manchestercity_jugadores = [
            self._crear_jugador("Ederson", "Moraes", 30, "portero", 0),
            self._crear_jugador("Kyle", "Walker", 33, "defensa", 2),
            self._crear_jugador("Ruben", "Dias", 26, "defensa", 2),
            self._crear_jugador("John", "Stones", 29, "defensa", 2),
            self._crear_jugador("Nathan", "Ake", 28, "defensa", 2),
            self._crear_jugador("Rodri", "Hernandez", 27, "mediocampista", 8),
            self._crear_jugador("Kevin", "De Bruyne", 32, "mediocampista", 8),
            self._crear_jugador("Bernardo", "Silva", 29, "mediocampista", 8),
            self._crear_jugador("Erling", "Haaland", 23, "delantero", 60),
            self._crear_jugador("Phil", "Foden", 23, "delantero", 20),
            self._crear_jugador("Julian", "Alvarez", 23, "delantero", 25),
            self._crear_jugador("Stefan", "Ortega", 31, "portero", 0)
        ]

        manchestercity = Equipo(
            nombre="Manchester City",
            entrenador=self._crear_entrenador("Pep", "Guardiola", 53, 15),
            jugadores=manchestercity_jugadores
        )

        self.liga.equipos.append(manchestercity)

        arsenal_jugadores = [
            self._crear_jugador("Aaron", "Ramsdale", 25, "portero", 0),
            self._crear_jugador("Ben", "White", 26, "defensa", 2),
            self._crear_jugador("William", "Saliba", 22, "defensa", 2),
            self._crear_jugador("Gabriel", "Magalhaes", 25, "defensa", 2),
            self._crear_jugador("Oleksandr", "Zinchenko", 26, "defensa", 2),
            self._crear_jugador("Martin", "Odegaard", 24, "mediocampista", 15),
            self._crear_jugador("Declan", "Rice", 24, "mediocampista", 8),
            self._crear_jugador("Kai", "Havertz", 24, "mediocampista", 8),
            self._crear_jugador("Bukayo", "Saka", 22, "delantero", 26),
            self._crear_jugador("Gabriel", "Jesus", 26, "delantero", 20),
            self._crear_jugador("Gabriel", "Martinelli", 22, "delantero", 15),
            self._crear_jugador("David", "Raya", 28, "portero", 0)
        ]

        arsenal = Equipo(
            nombre="Arsenal",
            entrenador=self._crear_entrenador("Mikel", "Arteta", 42, 5),
            jugadores=arsenal_jugadores
        )

        self.liga.equipos.append(arsenal)

        liverpool_jugadores = [
            self._crear_jugador("Alisson", "Becker", 31, "portero", 0),
            self._crear_jugador("Trent", "Alexander-Arnold", 25, "defensa", 2),
            self._crear_jugador("Virgil", "van Dijk", 32, "defensa", 2),
            self._crear_jugador("Joel", "Matip", 32, "defensa", 2),
            self._crear_jugador("Andy", "Robertson", 29, "defensa", 2),
            self._crear_jugador("Dominik", "Szoboszlai", 23, "mediocampista", 8),
            self._crear_jugador("Alexis", "Mac Allister", 24, "mediocampista", 15),
            self._crear_jugador("Curtis", "Jones", 22, "mediocampista", 8),
            self._crear_jugador("Mohamed", "Salah", 31, "delantero", 40),
            self._crear_jugador("Darwin", "Nunez", 24, "delantero", 26),
            self._crear_jugador("Luis", "Diaz", 26, "delantero", 20),
            self._crear_jugador("Caoimhin", "Kelleher", 25, "portero", 0)
        ]

        liverpool = Equipo(
            nombre="Liverpool",
            entrenador=self._crear_entrenador("Arne", "Slot", 46, 7),
            jugadores=liverpool_jugadores
        )

        self.liga.equipos.append(liverpool)

        chelsea_jugadores = [
            self._crear_jugador("Robert", "Sanchez", 26, "portero", 0),
            self._crear_jugador("Reece", "James", 23, "defensa", 2),
            self._crear_jugador("Thiago", "Silva", 39, "defensa", 2),
            self._crear_jugador("Ben", "Chilwell", 26, "defensa", 2),
            self._crear_jugador("Wesley", "Fofana", 22, "defensa", 2),
            self._crear_jugador("Enzo", "Fernandez", 22, "mediocampista", 8),
            self._crear_jugador("Moises", "Caicedo", 22, "mediocampista", 8),
            self._crear_jugador("Conor", "Gallagher", 23, "mediocampista", 8),
            self._crear_jugador("Christopher", "Nkunku", 26, "delantero", 18),
            self._crear_jugador("Nicolas", "Jackson", 22, "delantero", 23),
            self._crear_jugador("Raheem", "Sterling", 28, "delantero", 10),
            self._crear_jugador("Djordje", "Petrovic", 24, "portero", 0)
        ]

        chelsea = Equipo(
            nombre="Chelsea",
            entrenador=self._crear_entrenador("Enzo", "Maresca", 44, 4),
            jugadores=chelsea_jugadores
        )

        self.liga.equipos.append(chelsea)

        juventus_jugadores = [
            self._crear_jugador("Wojciech", "Szczesny", 33, "portero", 0),
            self._crear_jugador("Danilo", "Luiz", 32, "defensa", 2),
            self._crear_jugador("Bremer", "Silva", 26, "defensa", 5),
            self._crear_jugador("Federico", "Gatti", 25, "defensa", 2),
            self._crear_jugador("Alex", "Sandro", 32, "defensa", 2),
            self._crear_jugador("Manuel", "Locatelli", 25, "mediocampista", 8),
            self._crear_jugador("Adrien", "Rabiot", 28, "mediocampista", 8),
            self._crear_jugador("Weston", "McKennie", 25, "mediocampista", 8),
            self._crear_jugador("Federico", "Chiesa", 26, "delantero", 15),
            self._crear_jugador("Dusan", "Vlahovic", 23, "delantero", 20),
            self._crear_jugador("Moise", "Kean", 23, "delantero", 15),
            self._crear_jugador("Mattia", "Perin", 30, "portero", 0)
        ]

        juventus = Equipo(
            nombre="Juventus",
            entrenador=self._crear_entrenador("Thiago", "Motta", 42, 5),
            jugadores=juventus_jugadores
        )

        self.liga.equipos.append(juventus)

        inter_jugadores = [
            self._crear_jugador("Yann", "Sommer", 34, "portero", 0),
            self._crear_jugador("Benjamin", "Pavard", 27, "defensa", 2),
            self._crear_jugador("Stefan", "de Vrij", 31, "defensa", 2),
            self._crear_jugador("Alessandro", "Bastoni", 24, "defensa", 2),
            self._crear_jugador("Federico", "Dimarco", 25, "defensa", 2),
            self._crear_jugador("Nicolo", "Barella", 26, "mediocampista", 8),
            self._crear_jugador("Hakan", "Calhanoglu", 29, "mediocampista", 8),
            self._crear_jugador("Henrikh", "Mkhitaryan", 34, "mediocampista", 8),
            self._crear_jugador("Lautaro", "Martinez", 26, "delantero", 20),
            self._crear_jugador("Marcus", "Thuram", 26, "delantero", 20),
            self._crear_jugador("Marko", "Arnautovic", 34, "delantero", 20),
            self._crear_jugador("Emil", "Audero", 26, "portero", 0)
        ]

        inter = Equipo(
            nombre="Inter",
            entrenador=self._crear_entrenador("Simone", "Inzaghi", 48, 10),
            jugadores=inter_jugadores
        )

        self.liga.equipos.append(inter)



    def obtener_equipos(self) -> List[Equipo]:
        return self.liga.equipos

    def obtener_promedio_edad(self, nombre_equipo: str) -> float:
        for equipo in self.liga.equipos:
            if equipo.nombre.lower() == nombre_equipo.lower():
                edades = [jugador.edad for jugador in equipo.jugadores]
                return sum(edades) / len(edades)
        return 0

    def obtener_goleador(self, nombre_equipo: str) -> Optional[Jugador]:
        for equipo in self.liga.equipos:
            if equipo.nombre.lower() == nombre_equipo.lower():
                return max(equipo.jugadores, key=lambda x: x.goles)
        return None

    def filtrar_por_posicion(self, nombre_equipo: str, posicion: str) -> List[Jugador]:
        for equipo in self.liga.equipos:
            if equipo.nombre.lower() == nombre_equipo.lower():
                return [j for j in equipo.jugadores if j.posicion.lower() == posicion.lower()]
        return []