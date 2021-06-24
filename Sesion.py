import Usuario


class Sesion:
    usuario: Usuario
    pass

    def getEmpleadoEnSesion(self):
        return self.usuario.obtenerEmpleado()