#pip install fastapi
#pip intall uvicorn
#generar la URL para verificar la API
#uvicorn main: app --reload

#importar la clase FastAPI desde el paquete fatapi

from fastapi import FastAPI

#app es una variable que utiliza el servidor para ejecitar

app = FastAPI()

#Definimos las rutas o PATH
@app.get("/")
def inicio():

#lA API automaticamente convierte el JSON

    return {"mensaje":"Hola esta es mi API att Andrés Riaño"}

#main.py es el archivo principal que contiene la FastAPI


