from datetime import datetime
from datetime import time
import Exposicion
import ReservaVisita


class Sede:
    nombre: str
    cantMaximaVisitantes: int
    cantMaxPorGuia: int
    exposiciones: list[Exposicion]
    reservas: list[ReservaVisita]
    pass

    def mostrarNombre(self):
        return self.nombre

    def buscarExposiciones(self):
        exposicionesArray = []
        for exposicion in self.exposiciones:
            exposicionesArray.append(exposicion.getTempVigentes())
        return exposicionesArray

    def buscarDuracionExposiciones(self, expoSeleccionadas: list[Exposicion]):
        for exposicion in expoSeleccionadas:
            exposicion.buscarDuracionExtendidaObras()

    def buscarReservasParaFechaYHora(self, fechaHora: datetime):
        reservasArray = []
        for reservaObj in self.reservas:
            if reservaObj.obtenerAlumnosEnReserva(fechaHora):
                reservasArray.append(reservaObj.cantidadAlumnos)
        return reservasArray

    def getCantMaximaVisitantes(self):
        return self.cantMaximaVisitantes

    def getCantMaxPorGuia(self):
        return self.getCantMaxPorGuia()
