from fastapi import FastAPI

app = FastAPI()

#=================LISTA DE USUARIOS====================

usuarios = [
    {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Perez",
        "telefono": "324567890",
        "edad": 35
    },

    {
        "id": 2,
        "nombre": "María",
        "apellido": "Goméz",
        "telefono": "3229087654",
        "edad": 35
    }
]

@app.get("/")
def inicio():
    return "Bienvenido al programa de usuarios"

#===============RUTA PRINCIPAL===========================

@app.get("/listadeusuarios")
def obtener_usuario():
    return usuarios

#=================AGREGAR USUARIO=========================

@app.post("/agregarusuarios")
def agregar_usuarios(
    nombre:str,
    apellido:str,
    telefono:str,
    edad:int
):
    nuevo_id = len(usuarios) + 1

    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "edad": edad

    }

    usuarios.append(nuevo_usuario)

    return {
        "mensaje": "Usuario agregado exitosamente",
        "usuario": nuevo_usuario
    }

#=================BUSCAR POR ID========================

@app.get("/listadeusuarios/{id}")
def obtener_usuario(id: int):

    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario

    return {
        "mensaje": "Usuario no encontrado"
    }



#=======================ELIMINAR USUARIO===================

@app.delete("/eliminarusuario/{id}")
def eliminar_usuario(id:int):
    for usuario in usuarios:

        if usuario["id"] == id:
            usuarios.remove(usuario)

            return {
                "mensaje": "Usuario eliminado exitosamente",
                "usuario": usuario
            }

    return{
        "mensaje": "Usuario no encontrado"
    }