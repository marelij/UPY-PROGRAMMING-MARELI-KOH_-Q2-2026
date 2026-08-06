"""
Classwork #16 - Recursive Functions
Unit 4 - UPY Programming

This file implements the recursive functions covered in the tutorial:
recursiva, fibonacci, factorial, multiplicacion_recursiva,
division_entera_recursiva, potencia_recursiva, serie_collatz, aplanar_json

Every function validates its input BEFORE recursing so that invalid input
(negative numbers, wrong types, lists instead of dicts, etc.) is handled
gracefully with try/except instead of crashing the program or causing an
infinite / uncontrolled recursion (RecursionError).
"""


# 1. Basic recursion example — recursiva(n)
def recursiva(n):
    """Cuenta regresiva desde n hasta 1 usando recursión."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")

        if n == 0:
            print("¡Despegue!")
            return
        else:
            print(n)
            recursiva(n - 1)
    except (TypeError, ValueError) as e:
        print(f"Error en recursiva: {e}")


# 2. Fibonacci — fibonacci(n)
def fibonacci(n):
    """Regresa el n-ésimo número de la serie de Fibonacci."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except (TypeError, ValueError) as e:
        print(f"Error en fibonacci: {e}")
        return None


# 3. Factorial — factorial(n)
def factorial(n):
    """Regresa n! (n factorial) usando recursión."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n < 0:
            raise ValueError("n no puede ser negativo")

        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    except (TypeError, ValueError) as e:
        print(f"Error en factorial: {e}")
        return None


# 4. Recursive multiplication — multiplicacion_recursiva(a, b)
def multiplicacion_recursiva(a, b):
    """Multiplica a * b usando solo sumas recursivas."""
    try:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a y b deben ser números enteros")

        if b < 0:
            return -multiplicacion_recursiva(a, -b)
        if b == 0:
            return 0
        else:
            return a + multiplicacion_recursiva(a, b - 1)
    except TypeError as e:
        print(f"Error en multiplicacion_recursiva: {e}")
        return None


# 5. Recursive integer division — division_entera_recursiva(dividendo, divisor)
def division_entera_recursiva(dividendo, divisor):
    """Regresa el cociente entero de dividendo / divisor usando restas recursivas."""
    try:
        if not isinstance(dividendo, int) or not isinstance(divisor, int):
            raise TypeError("dividendo y divisor deben ser números enteros")
        if divisor == 0:
            raise ZeroDivisionError("El divisor no puede ser 0")
        if dividendo < 0 or divisor < 0:
            raise ValueError("Esta función solo soporta valores positivos")

        if dividendo < divisor:
            return 0
        else:
            return 1 + division_entera_recursiva(dividendo - divisor, divisor)
    except (TypeError, ZeroDivisionError, ValueError) as e:
        print(f"Error en division_entera_recursiva: {e}")
        return None


# 6. Power — potencia_recursiva(base, exponente)
def potencia_recursiva(base, exponente):
    """Regresa base elevado a exponente usando recursión."""
    try:
        if not isinstance(base, (int, float)) or isinstance(base, bool):
            raise TypeError("base debe ser un número")
        if not isinstance(exponente, int) or isinstance(exponente, bool):
            raise TypeError("exponente debe ser un número entero")
        if exponente < 0:
            # Matemáticamente daría 1 / base**|exponente|, pero la versión
            # recursiva del tutorial nunca llega al caso base con
            # exponentes negativos (nunca llega a 0), así que se rechaza
            # explícitamente para evitar un RecursionError.
            raise ValueError(
                "exponente negativo no soportado: nunca se alcanza el caso base (0)"
            )

        if exponente == 0:
            return 1
        else:
            return potencia_recursiva(base, exponente - 1) * base
    except (TypeError, ValueError) as e:
        print(f"Error en potencia_recursiva: {e}")
        return None


# 7. Collatz sequence — serie_collatz(n)
def serie_collatz(n):
    """Imprime la secuencia de Collatz empezando en n hasta llegar a 1."""
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n debe ser un número entero")
        if n <= 0:
            # n = 0 nunca llega a 1 (0 // 2 = 0 por siempre -> recursión infinita)
            # los negativos tampoco llegan nunca exactamente a 1
            raise ValueError("n debe ser un entero positivo mayor que 0")

        if n == 1:
            print("END!")
            return 0
        else:
            if n % 2 == 0:
                print(n // 2)
                return serie_collatz(n // 2)
            else:
                print(3 * n + 1)
                return serie_collatz(3 * n + 1)
    except (TypeError, ValueError) as e:
        print(f"Error en serie_collatz: {e}")
        return None


# 8. Flattening a JSON — aplanar_json(diccionario, clave_padre, separador)
def aplanar_json(diccionario, clave_padre='', separador='.'):
    """Aplana un diccionario anidado en un diccionario de un solo nivel."""
    try:
        if not isinstance(diccionario, dict):
            # Ej: si se pasa una lista en vez de un dict, .items() no existe
            raise AttributeError(
                f"aplanar_json solo acepta diccionarios, se recibió {type(diccionario).__name__}"
            )

        elementos = []
        for key, value in diccionario.items():
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
            if isinstance(value, dict):
                elementos.extend(aplanar_json(value, nueva_llave, separador).items())
            else:
                # Nota: las listas (como "tags": [1, 2, 3]) NO se aplanan,
                # se guardan tal cual como valor. Colisiones de llaves
                # (ej. "a.b" vs "a":{"b":..}) se sobrescriben en silencio,
                # tal como en la implementación original del tutorial.
                elementos.append((nueva_llave, value))
        return dict(elementos)
    except AttributeError as e:
        print(f"Error en aplanar_json: {e}")
        return {}


if __name__ == "__main__":
    print("--- recursiva ---")
    recursiva(5)
    recursiva(-3)          # Fail case -> manejado, no crashea
    recursiva("hola")      # Fail case -> manejado, no crashea

    print("\n--- fibonacci ---")
    print(fibonacci(7))
    print(fibonacci(-1))   # Fail case

    print("\n--- factorial ---")
    print(factorial(5))
    print(factorial(-2))   # Fail case

    print("\n--- multiplicacion_recursiva ---")
    print(multiplicacion_recursiva(4, 5))
    print(multiplicacion_recursiva(4, -3))
    print(multiplicacion_recursiva(4, "5"))  # Fail case

    print("\n--- division_entera_recursiva ---")
    print(division_entera_recursiva(17, 3))
    print(division_entera_recursiva(10, 0))   # Fail case

    print("\n--- potencia_recursiva ---")
    print(potencia_recursiva(2, 5))    # 32
    print(potencia_recursiva(5, 0))    # 1
    print(potencia_recursiva(2, -2))   # Fail case -> manejado

    print("\n--- serie_collatz ---")
    serie_collatz(6)
    serie_collatz(1)
    serie_collatz(0)       # Fail case -> manejado
    serie_collatz(-6)      # Fail case -> manejado

    print("\n--- aplanar_json ---")
    print(aplanar_json({"a": 1, "b": {"c": 2}}))
    print(aplanar_json({"a": {"b": {"c": 1}}}))
    print(aplanar_json(["a", "b", "c"]))          # Fail case -> manejado
    print(aplanar_json({"tags": [1, 2, 3]}))      # lista se guarda tal cual
    print(aplanar_json({"a.b": 1, "a": {"b": 2}}))  # colisión de llaves
