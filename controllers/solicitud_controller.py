from flask import Blueprint, request, jsonify
from services.solicitud_service import SolicitudService

solicitud_bp = Blueprint("solicitud_bp", __name__, url_prefix="/solicitudes")
service = SolicitudService()

# Listar todas las solicitudes
@solicitud_bp.route("/", methods=["GET"])
def listar():
    return jsonify(service.listar()), 200

# Buscar por ID
@solicitud_bp.route("/<int:id>", methods=["GET"])
def obtener_por_id(id):
    solicitud = service.buscar_por_id(id)
    if solicitud:
        return jsonify(solicitud), 200
    return jsonify({"error": "Solicitud no encontrada"}), 404

# Crear una nueva solicitud
@solicitud_bp.route("/", methods=["POST"])
def crear():
    data = request.get_json()
    return jsonify(service.crear(data)), 201

# Aprobar una solicitud
@solicitud_bp.route("/<int:id>/aprobar", methods=["PUT"])
def aprobar(id):
    return jsonify(service.aprobar(id)), 200

# Rechazar una solicitud
@solicitud_bp.route("/<int:id>/rechazar", methods=["PUT"])
def rechazar(id):
    return jsonify(service.rechazar(id)), 200

# Eliminar una solicitud
@solicitud_bp.route("/<int:id>", methods=["DELETE"])
def eliminar(id):
    return jsonify(service.eliminar(id)), 200
