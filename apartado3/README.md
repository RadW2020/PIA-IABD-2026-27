# Apartado 3 · Competición en Kaggle

Raúl Jiménez Martín

Competición elegida: **[Name That LLM](https://www.kaggle.com/competitions/name-that-llm)**

## 1. Cuenta de Kaggle

No he tenido que crear una cuenta nueva: ya tenía una desde hace más de 9 años, con el usuario `radw2020`. En el perfil se ve la antigüedad («Joined 9 years ago»).

![Perfil de Kaggle con la cuenta creada hace 9 años](capturas/01-cuenta.png)

## 2. Acceso a una competición activa

Desde la sección **Competitions** busqué la competición. Name That LLM es una *Featured Code Competition* con 50.000 $ en premios y le quedan 3 meses para cerrar, así que está activa.

![Búsqueda de la competición en el listado de Competitions](capturas/02-competiciones-activas.png)

En la página de la competición (pestaña **Overview**) se explica el reto: identificar cuál de 18 modelos de lenguaje ha escrito cada texto. Es un problema de clasificación que se evalúa con *balanced accuracy*. Arriba aparece un aviso de que la competición exige verificar la identidad.

![Página Overview de la competición](capturas/03-competicion.png)

Antes de poder unirme a la competición, Kaggle me pidió verificar mi identidad en dos pasos: primero un reconocimiento facial a través de Persona, el servicio de verificación que usa Kaggle, y después un código enviado por SMS a mi móvil. En la captura he tapado el número de teléfono.

![Verificación de la cuenta por SMS](capturas/04a-verificacion-sms.png)

Una vez verificado, al pulsar **Join Competition** aparecen las reglas, que hay que aceptar con **I Understand and Accept**. Sin este paso Kaggle no deja descargar los datos.

![Aceptación de las reglas de la competición](capturas/04b-reglas.png)

Con las reglas aceptadas aparece la confirmación y se habilitan las pestañas **Team** y **Submissions**.

![Reglas aceptadas](capturas/04c-reglas-aceptadas.png)

## 3. Descarga del dataset

En la pestaña **Data** está la descripción del dataset: 3 ficheros (2,14 MB en total) con licencia CC BY-SA 4.0.

- `train.csv`: conjunto de entrenamiento, 2699 textos escritos para 150 *prompts*.
- `test.csv`: solo 3 filas de ejemplo; el test real (~4000 textos) está oculto y se ejecuta al enviar el código.
- `sample_submission.parquet`: ejemplo del formato de envío (`id`, `model`).

![Pestaña Data de la competición](capturas/05-data.png)

Kaggle ofrece descargar los datos con la librería `kagglehub` o como zip. Yo usé **Download as zip**.

![Opciones de descarga del dataset](capturas/06-descarga.png)

## 4. Dataset descargado

Al descomprimir el zip quedan los tres ficheros:

![Ficheros del dataset descomprimidos](capturas/07-ficheros.png)

Abrí `train.csv` en VS Code para ver su contenido. Cada fila es un texto generado por un modelo, con las columnas `id`, `prompt_id`, `text` y `model` (el modelo que lo escribió, que es lo que hay que predecir).

![Primeras filas de train.csv](capturas/08-contenido.png)

El conjunto de entrenamiento está equilibrado: 150 textos por cada uno de los 18 modelos (149 en uno de ellos), de unas 115 palabras de media. Los modelos son de Anthropic, Google, OpenAI, Qwen, Moonshot (Kimi) y Z.ai (GLM).

El dataset no se sube al repositorio (está en el `.gitignore`); aquí solo van las capturas.
