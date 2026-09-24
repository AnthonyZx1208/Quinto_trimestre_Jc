from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def inicio():
    return {"texto": "aqui estamos en la raiz principal del proyecto '/'"}

@app.get("/cliente")
def cliente():
    return {
        "id":1234,
        "nombre": "Jeimy",
        "programa": "ADSO"
    }

@app.get("/roles")
def roles():
    return{
        "idRoles": 1,
        "nombreRol": "Administrador",
        "descripcionRol": "Tiene acceso a toda la app"
    }

@app.get("/usuarios")
def usuarios():
    return{
        "idUsuarios": 2,
        "nombreUsuarios": "José",
        "ApellidoUsuario": "Goméz",
        "tipoDocumento": "Cedula de ciudadania",
        "numeroDocumento": 1027632234,
        "correo": "joselito@gmail.com"
    }

@app.get("/tipoDocumento")
def tipoDocumento():
    return{
        "idTipoDocumento": 3,
        "nombreTpDoc": "Cédula de ciudadania",
        "descripcioTpDoc": "Para ciudadanos mayores de 18 años"
    }