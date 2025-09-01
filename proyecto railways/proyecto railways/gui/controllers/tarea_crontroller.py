from models import crear_tarea

class TareaController :
    @staticmethod
    def agregar_tarea (datos): #investigar como podemos asignar tareas al usuario (session = usuario ==> insert en tareas nombre = usuario 
        try:
            crear_tarea(
                nombre = datos ["nombre"],
                id_usuario = int(datos["id_usuarios"]),
                porcentaje= int(datos["porcentaje"])
            )
            return True

        except ValueError(self, id_usuario):
            raise ValueError("ID y Porcentajes deben ser numeros ")
        except Exception as e :
            raise Exception (f"Error al agregar tarea: {str(e)}")
        finally:
            print ("gracias") 
        
