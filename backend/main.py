from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

modelo = tf.keras.models.load_model("modelo_adivina_mi_dibujo.h5")
categorias = ["cat", "house", "car", "tree", "sun"]

@app.get("/")
def home():
    return {"mensaje": "API de Adivina mi Dibujo funcionando"}

def preparar_imagen(imagen: Image.Image) -> Image.Image:
    ancho, alto = imagen.size
    lado = max(ancho, alto)
    fondo = Image.new("L", (lado, lado), color=0)
    fondo.paste(imagen, ((lado - ancho) // 2, (lado - alto) // 2))
    return fondo.resize((28, 28))

@app.post("/predecir")
async def predecir(file: UploadFile = File(...)):
    contenido = await file.read()
    imagen = Image.open(io.BytesIO(contenido)).convert("L")
    imagen = preparar_imagen(imagen)

    arr = np.array(imagen).astype("float32") / 255.0
    arr = arr.reshape(1, 28, 28, 1)

    prediccion = modelo.predict(arr)[0]
    top_indices = prediccion.argsort()[-3:][::-1]
    resultados = [
        {"categoria": categorias[i], "confianza": float(prediccion[i])}
        for i in top_indices
    ]

    return {"predicciones": resultados}