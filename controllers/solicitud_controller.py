from flask import Blueprint, request, jsonify
import services.solicitud_service as service

solicitud_bp = Blueprint("solicitud_bp", __name__)

# Listar todas las solicitudes
@solicitud_bp.route("/solicitudes", methods=["GET"])
def listar():
    return jsonify(service.listar_solicitudes()), 200

# Crear una nueva solicitud
@solicitud_bp.route("/solicitudes", methods=["POST"])
def crear():
    data = request.get_json()
    nueva = service.crear_solicitud(data)
    return jsonify(nueva), 201

# Aprobar una solicitud
@solicitud_bp.route("/solicitudes/<int:id>/aprobar", methods=["PUT"])
def aprobar(id):
    solicitud = service.aprobar_solicitud(id)
    if solicitud:
        return jsonify({"mensaje": "Solicitud aprobada", "solicitud": solicitud}), 200
    return jsonify({"error": "No encontrada o ya procesada"}), 404
# Rechazar una solicitud
@solicitud_bp.route("/solicitudes/<int:id>/rechazar", methods=["PUT"])
def rechazar(id):
    solicitud = service.rechazar_solicitud(id)
    if solicitud:
        return jsonify({"mensaje": "Solicitud rechazada", "solicitud": solicitud}), 200
    return jsonify({"error": "No encontrada o ya procesada"}), 404

# Eliminar una solicitud
@solicitud_bp.route("/solicitudes/<int:id>", methods=["DELETE"])
def eliminar(id):
    exito = service.eliminar_solicitud(id)
    if exito:
        return jsonify({"mensaje": "Solicitud eliminada"}), 200
    return jsonify({"error": "Notificación no encontrada"}), 404