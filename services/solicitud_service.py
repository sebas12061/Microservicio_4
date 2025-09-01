from repositories.solicitud_repository import solicitudes, contador_id
from models.solicitud import Solicitud

def listar_solicitudes():
    return [s.to_dict() for s in solicitudes]

def crear_solicitud(data):
    global contador_id
    nueva = Solicitud(contador_id, data["nombre"], data["categoria"], data["ubicacion"])
    solicitudes.append(nueva)
    contador_id += 1
    return nueva.to_dict()

def aprobar_solicitud(id):
    for s in solicitudes:
        if s.id == id and s.estado == "pendiente":
            s.estado = "aceptada"
            return s.to_dict()
    return None

def rechazar_solicitud(id):
    for s in solicitudes:
        if s.id == id and s.estado == "pendiente":
            s.estado = "rechazada"
            return s.to_dict()
    return None
