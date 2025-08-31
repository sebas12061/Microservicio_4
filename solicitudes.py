from flask import Flask, jsonify, request

app = Flask(__name__)

solicitudes = []
contador_id = 1

# Ver todas las solicitudes
@app.route("/solicitudes", methods=["GET"])
def listar_solicitudes():
    return jsonify(solicitudes), 200

# Crear nueva solicitud (llamado por mapas.py)
@app.route("/solicitudes", methods=["POST"])
def crear_solicitud():
    global contador_id
    data = request.get_json()
    nueva_solicitud = {
        "id": contador_id,
        "nombre": data.get("nombre"),
        "categoria": data.get("categoria"),
        "ubicacion": data.get("ubicacion"),
        "estado": "pendiente"
    }
    solicitudes.append(nueva_solicitud)
    contador_id += 1
    return jsonify(nueva_solicitud), 201

# Aprobar solicitud
@app.route("/solicitudes/<int:id>/aprobar", methods=["PUT"])
def aprobar_solicitud(id):
    for solicitud in solicitudes:
        if solicitud["id"] == id and solicitud["estado"] == "pendiente":
            solicitud["estado"] = "aceptada"
            return jsonify({"mensaje": "Solicitud aprobada"}), 200
    return jsonify({"error": "Solicitud no encontrada o ya procesada"}), 404

# Rechazar solicitud
@app.route("/solicitudes/<int:id>/rechazar", methods=["PUT"])
def rechazar_solicitud(id):
    for solicitud in solicitudes:
        if solicitud["id"] == id and solicitud["estado"] == "pendiente":
            solicitud["estado"] = "rechazada"
            return jsonify({"mensaje": "Solicitud rechazada"}), 200
    return jsonify({"error": "Solicitud no encontrada o ya procesada"}), 404

if __name__ == "__main__":
    app.run(port=5007, debug=True)
