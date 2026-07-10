import math
import logging

### Configuracion del logging: los mensajes se guardan en un archivo,
### con fecha, nivel de severidad y el mensaje
logging.basicConfig(
    filename="numerical_integration.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


### Excepciones personalizadas para las dos cosas que pueden salir mal
### al elegir opciones o al definir el intervalo
class OpcionInvalidaError(Exception):
    def _init_(self, opcion, opciones_validas):
        self.opcion = opcion
        super()._init_(f"'{opcion}' no es una opcion valida. Elija entre: {list(opciones_validas)}")


class IntervaloInvalidoError(Exception):
    pass


def calcular_area(f, a, b, n, metodo):
    ### Calcula el area aproximada bajo la curva con el metodo elegido.
    ### Es el mismo for loop para los 4 metodos, cambiando el punto donde
    ### se evalua la funcion en cada rectangulo (o trapecio para TRAP)
    h = (b - a) / n
    area = 0.0

    if metodo == 'TRAP':
        area += (h / 2) * f(a)
        for i in range(1, n):
            xi = a + i * h
            area += h * f(xi)
        area += (h / 2) * f(b)
    else:
        shift = 1 if metodo == 'RRM' else 0
        constante = h / 2 if metodo == 'MRM' else 0
        for i in range(shift, n + shift):
            xi = a + i * h
            area += h * f(xi + constante)

    return area


# INPUT
### Lista de funciones disponibles. Cada una guarda su formula f, su
### antiderivada F (para calcular el valor exacto) y el dominio minimo
### que debe respetar el intervalo (None si no tiene restriccion)
funciones = {
    '1': {
        'nombre': 'P1: f(x) = x^2 + 2x - 3',
        'f': lambda x: x**2 + 2 * x - 3,
        'F': lambda x: (x*3) / 3 + x*2 - 3 * x,
        'dominio_min': None
    },
    '2': {
        'nombre': 'P2: f(x) = 3x^3 - x^2 + 5',
        'f': lambda x: 3 * x*3 - x*2 + 5,
        'F': lambda x: (3 * x*4) / 4 - (x*3) / 3 + 5 * x,
        'dominio_min': None
    },
    '3': {
        'nombre': 'T1: f(x) = sin(x)',
        'f': lambda x: math.sin(x),
        'F': lambda x: -math.cos(x),
        'dominio_min': None
    },
    '4': {
        'nombre': 'T2: f(x) = cos(x) + 1',
        'f': lambda x: math.cos(x) + 1,
        'F': lambda x: math.sin(x) + x,
        'dominio_min': None
    },
    '5': {
        'nombre': 'Tr1: f(x) = e^x',
        'f': lambda x: math.exp(x),
        'F': lambda x: math.exp(x),
        'dominio_min': None
    },
    '6': {
        'nombre': 'Tr2: f(x) = ln(x)',
        'f': lambda x: math.log(x),
        'F': lambda x: x * math.log(x) - x,
        'dominio_min': 0
    }
}

print("Funciones disponibles:")
for clave in funciones:
    print(f"  {clave}. {funciones[clave]['nombre']}")

### Pedimos la funcion en un ciclo hasta que sea una opcion valida
funcion_valida = False
while not funcion_valida:
    try:
        opcion_funcion = input("Elija una funcion (1-6): ").strip()
        if opcion_funcion not in funciones:
            raise OpcionInvalidaError(opcion_funcion, funciones.keys())
    except OpcionInvalidaError as e:
        logging.warning(str(e))
        print(e)
    else:
        funcion_valida = True

funcion_elegida = funciones[opcion_funcion]

### Pedimos el intervalo, validando que sean numeros, que a < b, y que
### respeten el dominio de la funcion (ln(x) exige x > 0)
intervalo_valido = False
while not intervalo_valido:
    try:
        a = float(input("Ingrese el limite izquierdo del intervalo (a): "))
        b = float(input("Ingrese el limite derecho del intervalo (b): "))

        if a >= b:
            raise IntervaloInvalidoError("El limite izquierdo debe ser menor que el derecho")

        dominio_min = funcion_elegida['dominio_min']
        if dominio_min is not None and a <= dominio_min:
            raise IntervaloInvalidoError(
                f"Esta funcion requiere que el intervalo comience en un valor mayor a {dominio_min}"
            )

    except ValueError:
        logging.warning("Se ingreso un limite del intervalo no numerico")
        print("Error: debe ingresar un numero valido")
    except IntervaloInvalidoError as e:
        logging.warning(str(e))
        print(f"Intervalo invalido: {e}")
    else:
        intervalo_valido = True

### Pedimos el modo de operacion
print("\nModos disponibles:")
print("  1. Default (n = 100, metodo del punto medio)")
print("  2. Custom (usted elige n y el metodo)")
print("  3. Auto-adjust (usted elige el error maximo permitido)")

modos_validos = ['1', '2', '3']
modo_valido = False
while not modo_valido:
    try:
        modo = input("Elija un modo (1-3): ").strip()
        if modo not in modos_validos:
            raise OpcionInvalidaError(modo, modos_validos)
    except OpcionInvalidaError as e:
        logging.warning(str(e))
        print(e)
    else:
        modo_valido = True

metodos_validos = ['LRM', 'RRM', 'MRM', 'TRAP']

if modo == '2':
    ### Modo Custom: el usuario define n y el metodo
    n_valido = False
    while not n_valido:
        try:
            n = int(input("Ingrese el numero de subintervalos (n): "))
            if n <= 0:
                raise ValueError("n debe ser un entero positivo")
        except ValueError as e:
            logging.warning(f"n invalido: {e}")
            print(f"Error: {e}")
        else:
            n_valido = True

    metodo_valido = False
    while not metodo_valido:
        try:
            metodo = input("Elija el metodo (LRM/RRM/MRM/TRAP): ").strip().upper()
            if metodo not in metodos_validos:
                raise OpcionInvalidaError(metodo, metodos_validos)
        except OpcionInvalidaError as e:
            logging.warning(str(e))
            print(e)
        else:
            metodo_valido = True

elif modo == '3':
    ### Modo Auto-adjust: el usuario define el error relativo maximo
    ### permitido (%) y el programa busca el n minimo que lo cumple
    umbral_valido = False
    while not umbral_valido:
        try:
            umbral_error = float(input("Ingrese el error relativo maximo permitido (%): "))
            if umbral_error <= 0:
                raise ValueError("El umbral de error debe ser mayor que 0")
        except ValueError as e:
            logging.warning(f"Umbral invalido: {e}")
            print(f"Error: {e}")
        else:
            umbral_valido = True
    metodo = 'MRM'  # el metodo del punto medio es el mas preciso de los cuatro

else:
    ### Modo Default
    n = 100
    metodo = 'MRM'


# PROCESS
f = funcion_elegida['f']
F = funcion_elegida['F']
area = None

try:
    ### El valor exacto se obtiene evaluando la antiderivada en los limites
    valor_exacto = F(b) - F(a)

    if modo == '3':
        ### Ciclo de convergencia: empezamos con n = 10 y lo vamos doblando
        ### hasta que el error relativo sea menor o igual al umbral pedido
        n = 10
        while True:
            area = calcular_area(f, a, b, n, metodo)
            error_relativo_actual = abs((valor_exacto - area) / valor_exacto) * 100
            if error_relativo_actual <= umbral_error:
                break
            n *= 2
    else:
        area = calcular_area(f, a, b, n, metodo)

except ZeroDivisionError as e:
    logging.error(f"Division entre cero al integrar: {e}")
    print("Error: ocurrio una division entre cero durante el calculo")
except (ValueError, OverflowError) as e:
    logging.error(f"Error matematico al integrar: {e}")
    print(f"Error matematico durante el calculo: {e}")
else:
    ### Solo llegamos aqui si el calculo termino sin ningun error
    error_absoluto = abs(valor_exacto - area)
    error_relativo = abs((valor_exacto - area) / valor_exacto) * 100 if valor_exacto != 0 else 0.0
finally:
    print("Calculo terminado.")


# OUTPUT
if area is not None:
    print(f"\nFuncion: {funcion_elegida['nombre']}")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Metodo: {metodo}   n: {n}")
    print(f"Valor numerico: {area:.4f}")
    print(f"Valor exacto:   {valor_exacto:.4f}")
    print(f"Error absoluto: {error_absoluto:.4f}")
    print(f"Error relativo: {error_relativo:.4f}%")
else:
    print("No se pudo calcular la integral debido a un error.")