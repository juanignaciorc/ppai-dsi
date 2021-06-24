class Estado:
    nombre: str
    pass

    def esAmbitoReserva(self):
        return 'Ambito reserva' == self.nombre

    def esPe(self):
        return 'Pendiente de confirmacion' == self.nombre