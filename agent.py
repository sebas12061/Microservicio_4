import asyncio
import json
import requests
from mirascope.core.gemini import gemini_call

BASE_URL = "http://127.0.0.1:5007/solicitudes"

# Prompt
PLANTILLA_PROMPT = """
Eres un asistente que interpreta instrucciones en español sobre solicitudes.
Debes devolver SIEMPRE un JSON válido con el siguiente formato:

{{ "accion": "listar" }}
{{ "accion": "aprobar" }}
{{ "accion": "rechazar" }}
{{ "accion": "obtener" }}
{{ "accion": "pendientes" }}
{{ "accion": "aprobadas" }}
{{ "accion": "rechazadas" }}

Instrucción: {instruccion}
"""

# Definimos función con decorador para que Gemini interprete
@gemini_call(model="gemini-1.5-flash")
def interpretar_con_gemini(texto: str) -> str:
    return PLANTILLA_PROMPT.format(instruccion=texto)

# Ejecutar acción contra el microservicio
def ejecutar_accion(accion: dict):
    try:

        if accion["accion"] == "pendientes":
            r = requests.get(f"{BASE_URL}/pendientes")
            return r.json()

        if accion["accion"] == "listar":
            r = requests.get(BASE_URL)
            return r.json()

        elif accion["accion"] == "aprobar":
            r = requests.put(f"{BASE_URL}/{accion['id']}/aprobar")
            return r.json()

        elif accion["accion"] == "rechazar":
            r = requests.put(f"{BASE_URL}/{accion['id']}/rechazar")
            return r.json()
        
        elif accion["accion"] == "aprobadas":
            r = requests.get(f"{BASE_URL}/aprobadas")
            return r.json()
        
        elif accion["accion"] == "rechazadas":
            r = requests.get(f"{BASE_URL}/rechazadas")
            return r.json()

        elif accion["accion"] == "obtener":
            r = requests.get(f"{BASE_URL}/{accion['id']}")
            return r.json()

        else:
            return {"error": "Acción no reconocida"}

    except Exception as e:
        return {"error": str(e)}

# Bucle principal
async def main():
    print("Agente de Solicitudes listo.")
    print("Escribe una instrucción en español (ej: 'Muéstrame las solicitudes pendientes'):")

    while True:
        instruccion = input("> ")
        if instruccion.lower() in ["salir", "exit", "quit"]:
            print("Hasta luego")
            break

        try:
            # Ejecutamos la función decorada
            respuesta = interpretar_con_gemini(instruccion)
            interpretado = respuesta.content

            try:
                accion = json.loads(interpretado)
            except json.JSONDecodeError:
                if "pendiente" in instruccion.lower():
                    accion = {"accion": "pendientes"}
                elif "aprobar" in instruccion.lower():
                    accion = {"accion": "aprobar", "id": 1}
                elif "rechazar" in instruccion.lower():
                    accion = {"accion": "rechazar", "id": 1}
                else:
                    accion = {"accion": "listar"}

            print("Acción interpretada:", accion)
            resultado = ejecutar_accion(accion)
            print("Respuesta del microservicio:", resultado)

        except Exception as e:
            print("Error en el agente:", str(e))


if __name__ == "__main__":
    asyncio.run(main())