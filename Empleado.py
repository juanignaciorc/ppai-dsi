import datetime

import AsignacionVisita
import Cargo
import HorarioEmpleado

class Empleado:
    horarioEmpleado: HorarioEmpleado
    cargo: Cargo
    asignacionVisita: AsignacionVisita
    pass

    def getGuiaDispEnHorario(self, horario: datetime):
        if self.cargo.esGuia():
            self.horarioEmpleado.dispEnFechaHoraReserva(horario)
        self.asignacionVisita.esAsignacionParaFechaHora()

