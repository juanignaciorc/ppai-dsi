class TipoVisita:
    nombre: str
    pass

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrarNombre(self):
        return self.nombre

e = TipoVisita('Tipo 1')
f = TipoVisita('Tipo 2')
print(e.mostrarNombre())
print(f.mostrarNombre())
