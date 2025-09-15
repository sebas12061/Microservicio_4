from repositories.solicitud_repository import SolicitudRepository

class SolicitudService:
    def __init__(self):
        self.repo = SolicitudRepository()

    def listar(self):
        return self.repo.obtener_todas()

    def buscar_por_id(self, id):
        return self.repo.obtener_por_id(id)

    def crear(self, data):
        return self.repo.crear(data)

    def aprobar(self, id):
        return self.repo.actualizar_estado(id, "aceptada")

    def rechazar(self, id):
        return self.repo.actualizar_estado(id, "rechazada")

    def eliminar(self, id):
        return self.repo.eliminar(id)
