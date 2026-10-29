"""
Problema 2: Frecuencia de palabras en un texto.

Objetivo:
Escribir una función que reciba por parámetro una lista de palabras y la ruta a
un fichero de texto y devuelva un diccionario que muestre cuántas veces
aparecen las distintas palabras de la lista en el fichero de texto.
Hacer un pequeño programa que la ponga a prueba.

Requisitos:
1. Eliminar signos de puntuación y convertir todo a minúsculas.
2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.
"""

import string
from pathlib import Path


def contar_frecuencia_palabras(palabras: list[str], ruta_fichero: str | Path) -> dict[str, int]:
    """
    Cuenta la frecuencia de aparición de una lista de palabras en un archivo de texto.

    Args:
        palabras (list[str]): Lista de palabras a buscar.
        ruta_fichero (str | Path): Ruta al archivo de texto.

    Returns:
        dict[str, int]: Diccionario con las palabras como clave y su frecuencia
                        como valor, ordenado alfabéticamente por palabra.
    """
    # 1. Signos de puntuación a suprimir (incluye signos propios del español como ¿, ¡, comillas y rayas)
    signos = string.punctuation + "¿¡«»“”‘’—–"
    tabla_limpieza = str.maketrans("", "", signos)

    # Normalizar las palabras de la lista recibida: minúsculas, sin puntuación y sin duplicados
    palabras_normalizadas = {
        p.lower().translate(tabla_limpieza).strip()
        for p in palabras
        if p.strip()
    }

    # Inicializar el diccionario con las palabras objetivo y frecuencia 0
    frecuencias: dict[str, int] = {palabra: 0 for palabra in palabras_normalizadas}

    # 2. Lectura y limpieza del fichero
    ruta = Path(ruta_fichero)
    if not ruta.is_file():
        raise FileNotFoundError(f"No se encontró el fichero en la ruta: {ruta.resolve()}")

    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Convertir a minúsculas y eliminar signos de puntuación del texto
    texto_limpio = contenido.lower().translate(tabla_limpieza)

    # Separar en palabras individuales por espacios/saltos de línea
    tokens = texto_limpio.split()

    # 3. Contar la frecuencia de las palabras objetivo
    for token in tokens:
        if token in frecuencias:
            frecuencias[token] += 1

    # Devolver el diccionario ordenado alfabéticamente por la palabra
    return dict(sorted(frecuencias.items()))


if __name__ == "__main__":
    # Ruta al archivo de prueba en el mismo directorio que este script
    directorio_actual = Path(__file__).resolve().parent
    ruta_ejemplo = directorio_actual / "ejemplo.txt"

    # Lista de palabras a buscar sobre el texto de Stanisław Lem (Solaris)
    palabras_a_buscar = [
        "para",
        "cosmos",
        "mundos",
        "espejos",
        "queremos",
        "robot",          # No aparece en el texto (frecuencia 0)
        "¿contacto?",     # Prueba de signos de puntuación
        "TIERRA"          # Prueba de mayúsculas (aparece como "Tierra" en el texto)
    ]

    print("=" * 60)
    print("PROGRAMA DE PRUEBA: FRECUENCIA DE PALABRAS")
    print("=" * 60)
    print(f"Fichero analizado: {ruta_ejemplo.name}")
    print(f"Palabras solicitadas: {palabras_a_buscar}\n")

    # Llamada a la función
    resultado = contar_frecuencia_palabras(palabras_a_buscar, ruta_ejemplo)

    # Requisito 3: Mostrar las palabras y sus frecuencias ordenadas por la palabra
    print("Resultados (ordenados alfabéticamente por la palabra):")
    print("-" * 40)
    print(f"{'Palabra':<20} | {'Frecuencia':<10}")
    print("-" * 40)
    for palabra, frecuencia in resultado.items():
        print(f"{palabra:<20} | {frecuencia:<10}")
    print("-" * 40)
    print(f"\nDiccionario devuelto:\n{resultado}")

