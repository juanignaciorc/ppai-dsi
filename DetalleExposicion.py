import Obra

class DetalleExposicion:
    obra: list[Obra]
    pass

    def buscarDuracExtObra(self):
        for obraObj in self.obra:
            obraObj.getDuracionExtendida()