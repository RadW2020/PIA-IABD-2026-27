"""
Problema 1: Procesamiento de una lista de enteros.

Objetivo:
1. Eliminar los números negativos de la lista.
2. Eliminar los valores duplicados (mantener elementos únicos).
3. Ordenar los números resultantes de menor a mayor.
"""

def procesar_numeros(lista: list[int | float]) -> list[int | float]:
    """
    Filtra números negativos, elimina duplicados y ordena de forma ascendente.

    Args:
        lista (list[int | float]): Lista de números de entrada.

    Returns:
        list[int | float]: Lista ordenada sin números negativos ni duplicados.
    """
    # Paso 1: Filtrar y quedarse únicamente con los números no negativos (>= 0)
    sin_negativos: list[int | float] = []
    for numero in lista:
        if numero >= 0:
            sin_negativos.append(numero)

    # Paso 2: Eliminar valores duplicados conservando una única aparición
    sin_duplicados: list[int | float] = []
    for numero in sin_negativos:
        if numero not in sin_duplicados:
            sin_duplicados.append(numero)

    # Paso 3: Ordenar la lista resultante de menor a mayor
    # (se puede usar sin_duplicados.sort() o sorted(sin_duplicados))
    resultado = sorted(sin_duplicados)

    return resultado


# Versión alternativa y compacta usando estructuras nativas (set y sorted):
def procesar_numeros_idiomatico(lista: list[int | float]) -> list[int | float]:
    """
    Versión idiomática en Python:
    - Comprensión de listas o generador para filtrar negativos (x >= 0)
    - set() para eliminar duplicados
    - sorted() para ordenar ascendentemente y retornar una lista
    """
    return sorted(set(x for x in lista if x >= 0))


if __name__ == "__main__":
    # Caso de prueba del enunciado:
    datos_prueba = [4, -1, 2, 4, 3, -5, 2]
    
    print("Lista original:", datos_prueba)
    
    resultado_academico = procesar_numeros(datos_prueba)
    print("Resultado (paso a paso):", resultado_academico)
    
    resultado_idiomatico = procesar_numeros_idiomatico(datos_prueba)
    print("Resultado (idiomático):", resultado_idiomatico)

