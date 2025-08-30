from model import crear_usuario

class usuarioController :
    @staticmethod
    def agregar_usuario (nombre):
        try:
            crear_usuario(
                nombre = nombre ["nombre"],
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
        
