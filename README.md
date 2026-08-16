# Adivina mi Dibujo

Sistema de Inteligencia Artificial que predice en tiempo real qué estás dibujando, mientras lo dibujás, entre 5 categorías: **cat, house, car, tree, sun**.


---

## Cómo funciona

1. Dibujás en un lienzo (canvas) con el mouse o el dedo.
2. Mientras dibujás, el frontend le manda el dibujo al backend cada ~400ms.
3. Un modelo de red neuronal convolucional (CNN), entrenado con el dataset **Quick, Draw!** de Google, predice a qué categoría pertenece.
4. Se muestran en pantalla las 3 predicciones más probables con su porcentaje de confianza.

---

## Estructura del repositorio

```
proyecto_adivina_mi_dibujo/
├── colab/
│   └── Arias_Examen_adiviana_mi_dibujo.ipynb   # Notebook de entrenamiento del modelo
├── backend/
│   ├── main.py                                  # API FastAPI que sirve el modelo
│   ├── requirements.txt                         # Dependencias de Python
│   └── modelo_adivina_mi_dibujo.h5               # Modelo entrenado (CNN)
├── frontend/
│   └── index.html                               # Interfaz de dibujo (canvas)
├── .gitignore
└── README.md
```

---

## Requisitos previos

- **Python 3.11** (TensorFlow no es compatible con versiones más nuevas como 3.13/3.14 al momento de este proyecto).
- Un navegador web moderno (Chrome, Edge, Firefox).

---

## Cómo ejecutar el proyecto

### 1. Backend (API con el modelo)

Abrí una terminal y ubicate en la carpeta `backend/`:

```bash
cd backend
```

Creá un entorno virtual con Python 3.11 (si tenés varias versiones de Python instaladas, usá `py -3.11` en Windows):

```bash
py -3.11 -m venv venv
```

Activá el entorno virtual:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Instalá las dependencias:

```bash
pip install -r requirements.txt
```

Levantá el servidor:

```bash
uvicorn main:app --reload
```

Si todo salió bien, vas a ver el mensaje `Application startup complete.` y el servidor va a quedar corriendo en:

```
http://127.0.0.1:8000
```

Podés verificar que la API funciona entrando a `http://127.0.0.1:8000/docs` (documentación interactiva generada por FastAPI).

**Importante:** dejá esa terminal abierta y corriendo mientras usás la aplicación — no cierres ni escribas otros comandos ahí.

### 2. Frontend (interfaz de dibujo)

Con el backend corriendo, abrí el archivo `frontend/index.html` directamente en tu navegador (doble clic, o clic derecho → Abrir con → tu navegador). No necesita instalación ni servidor propio.

### 3. Usar la aplicación

1. Dibujá en el recuadro negro con el mouse (o el dedo, si estás en un dispositivo táctil).
2. Las predicciones se van a actualizar automáticamente mientras dibujás.
3. Usá el botón **Borrar** para reiniciar el lienzo y probar otro dibujo.

---

## Sobre el modelo

- **Arquitectura:** CNN con 2 bloques Conv2D + MaxPooling, seguidos de una capa densa con Dropout.
- **Dataset:** [Quick, Draw!](https://quickdraw.withgoogle.com/data) de Google (dominio público), 3,500 imágenes por categoría.
- **Accuracy en test:** 95.66%
- **Entrenamiento:** ver notebook en `colab/` para el proceso completo (preprocesamiento, arquitectura, entrenamiento con EarlyStopping, evaluación).

Más detalle técnico (dataset, arquitectura, métricas y decisiones de diseño) en el informe técnico adjunto.

---

## Categorías soportadas

`cat` · `house` · `car` · `tree` · `sun`

Para mejores resultados, dibujá de forma simple y rápida — parecido a un garabato, no a una ilustración detallada — ya que así es como está compuesto el dataset de entrenamiento.
