def gcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Args:
        a (int): El primer número entero.
        b (int): El segundo número entero.

    Returns:
        int: El máximo común divisor de a y b.

    Raises:
        ValueError: Si alguno de los argumentos no es un número entero.
        ZeroDivisionError: Si alguno de los argumentos es cero.
    """
    # Verificar que los argumentos sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Ambos argumentos deben ser números enteros")

    # Verificar si alguno de los argumentos es cero
    if a == 0 or b == 0:
        raise ZeroDivisionError("No se puede calcular el máximo común divisor si uno de los números es cero")

    # Aplicar el algoritmo de Euclides para calcular el MCD
    while b != 0:
        a, b = b, a % b
    return abs(a)


# Ejemplo de uso
try:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    resultado = gcd(num1, num2)
    print("El máximo común divisor de", num1, "y", num2, "es:", resultado)
except ValueError as ve:
    print("Error:", ve)
except ZeroDivisionError as zde:
    print("Error:", zde)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
