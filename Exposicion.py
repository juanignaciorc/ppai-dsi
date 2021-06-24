from datetime import time
import DetalleExposicion
import PublicoDestino
import TipoExposicion

class Exposicion:
    tipoExposicion: TipoExposicion
    publicoDestino: PublicoDestino
    horarioHabilitado: time
    detalleExposicion: DetalleExposicion
    pass

    def getTempVigentes(self):
        return f'Es temporal: {self.tipoExposicion.esTemporal()} \n ' \
               f'Publico destino: {self.publicoDestino.getPublicoDestino()} \n ' \
               f'Horario Habilitado: {self.getHorarioHabilitado()}'


    def getHorarioHabilitado(self):
        return self.horarioHabilitado

    def buscarDuracionExtendidaObras(self):
        self.detalleExposicion.buscarDuracExtObra()
