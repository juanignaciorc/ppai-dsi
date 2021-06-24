import datetime


class HorarioEmpleado:
    horarioDesde: datetime
    horarioHasta: datetime
    pass

    def dispEnFechaHoraReserva(self, horario: datetime):
        return self.horarioDesde < horario < self.horarioHasta
