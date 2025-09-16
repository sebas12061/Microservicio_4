from repositories.solicitud_repository import SolicitudRepository

class SolicitudService:
    def __init__(self):
        self.repo = SolicitudRepository()

    # Listar solicitudes pendientes
    def pendientes(self):
        return self.repo.obtener_pendientes()
    # Listar todas las solicitudes
    def listar(self):
        return self.repo.obtener_todas()

    # Buscar por ID
    def buscar_por_id(self, id):
        return self.repo.obtener_por_id(id)

    # Crear una nueva solicitud
    def crear(self, data):
        return self.repo.crear(data)

    # Aprobar una solicitud
    def aprobar(self, id):
        return self.repo.actualizar_estado(id, "aceptada")

    # Rechazar una solicitud
    def rechazar(self, id):
        return self.repo.actualizar_estado(id, "rechazada")
    
    # Listar solicitudes aprobadas
    def aprobadas(self):
        return self.repo.obtener_aprobadas()

    # Listar solicitudes rechazadas
    def rechazadas(self):
        return self.repo.obtener_rechazadas()

    # Eliminar una solicitud
    def eliminar(self, id):
        return self.repo.eliminar(id)
