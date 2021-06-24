import datetime


class ReservaVisita:
    numeroReserva: int
    fechaHora: datetime
    cantidadAlumnos: int
    pass

    def obtenerAlumnosEnReserva(self, fechaHora: datetime):
        if(self.getFechaHoraReserva() == fechaHora):
            return self.getCantidadAlumnos()

    def getFechaHoraReserva(self):
        return self.fechaHora

    def getCantidadAlumnos(self):
        return self.cantidadAlumnos

    def getNumeroReserva(self):
        return self.numeroReserva