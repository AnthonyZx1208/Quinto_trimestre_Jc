from fastapi import FastAPI
app = FastAPI()

#GET
@app.get("/")
def inicio():
    return {"mensaje":"Página principal de pat o ruta raiz"}

#POST
@app.post("/saludar")
def saludar(datos: dict):
    return {
        "mensaje": f"Hola {datos['nombre']}, bienvenido a está pagina"
    }