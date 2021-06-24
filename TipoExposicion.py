class TipoExposicion:
    tipo: str
    pass

    def esTemporal(self):
        return self.tipo == 'temporal'
