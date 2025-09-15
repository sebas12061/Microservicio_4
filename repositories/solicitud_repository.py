from models.solicitud import Solicitud
from database import get_connection

class SolicitudRepository:
    def obtener_todas(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM solicitudes")
        rows = cursor.fetchall()
        conn.close()
        return [Solicitud(**row).to_dict() for row in rows]

    def obtener_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM solicitudes WHERE id = %s", (id,))
        row = cursor.fetchone()
        conn.close()
        return Solicitud(**row).to_dict() if row else None

    def crear(self, data):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO solicitudes (nombre, categoria, ubicacion, estado) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data["nombre"], data["categoria"], data["ubicacion"], "pendiente"))
        conn.commit()
        conn.close()
        return {"mensaje": "Solicitud creada con éxito"}

    def actualizar_estado(self, id, nuevo_estado):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE solicitudes SET estado = %s WHERE id = %s"
        cursor.execute(query, (nuevo_estado, id))
        conn.commit()
        conn.close()
        return {"mensaje": f"Solicitud {nuevo_estado}"}
