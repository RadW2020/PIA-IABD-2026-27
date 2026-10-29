"""
Problema 3: Trabajo con conjuntos.

Objetivo:
Escribir una función que reciba dos listas de enteros y devuelva un diccionario
con la siguiente información (es obligatorio usar conjuntos para calcularlos):
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto, pero no en ambos).
"""


def operaciones_conjuntos(lista1: list[int], lista2: list[int]) -> dict[str, set[int]]:
    """
    Calcula la intersección, unión y diferencia simétrica entre dos listas de enteros
    utilizando la estructura de datos set (conjunto).

    Args:
        lista1 (list[int]): Primera lista de números enteros.
        lista2 (list[int]): Segunda lista de números enteros.

    Returns:
        dict[str, set[int]]: Diccionario con los resultados de las operaciones:
            - 'interseccion': Elementos comunes en ambos conjuntos.
            - 'union': Todos los elementos únicos de ambos conjuntos.
            - 'diferencia_simetrica': Elementos presentes en uno u otro, pero no en ambos.
    """
    # Conversión obligatoria de las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # 1. Intersección: elementos que pertenecen a ambos conjuntos
    # Equivale al operador: conjunto1 & conjunto2
    interseccion = conjunto1.intersection(conjunto2)

    # 2. Unión: todos los elementos presentes en cualquiera de los conjuntos (sin duplicados)
    # Equivale al operador: conjunto1 | conjunto2
    union = conjunto1.union(conjunto2)

    # 3. Diferencia simétrica: elementos que están en conjunto1 o en conjunto2, pero no en ambos
    # Equivale al operador: conjunto1 ^ conjunto2
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

    return {
        "interseccion": interseccion,
        "union": union,
        "diferencia_simetrica": diferencia_simetrica,
    }


if __name__ == "__main__":
    # Listas de enteros de prueba con elementos repetidos y compartidos
    lista_a = [1, 2, 2, 3, 4, 5, 6]
    lista_b = [4, 5, 6, 6, 7, 8, 9]

    print("=" * 60)
    print("PROGRAMA DE PRUEBA: OPERACIONES CON CONJUNTOS")
    print("=" * 60)
    print(f"Lista 1 original: {lista_a}")
    print(f"Lista 2 original: {lista_b}")
    print(f"Conjunto 1 (set(lista_a)): {set(lista_a)}")
    print(f"Conjunto 2 (set(lista_b)): {set(lista_b)}")
    print("-" * 60)

    # Llamada a la función principal
    resultado = operaciones_conjuntos(lista_a, lista_b)

    print("Resultados obtenidos en el diccionario:")
    print(f"1. Intersección (comunes):             {resultado['interseccion']}")
    print(f"2. Unión (todos sin duplicados):       {resultado['union']}")
    print(f"3. Diferencia simétrica (no comunes):  {resultado['diferencia_simetrica']}")
    print("-" * 60)
    print(f"Diccionario devuelto:\n{resultado}")

