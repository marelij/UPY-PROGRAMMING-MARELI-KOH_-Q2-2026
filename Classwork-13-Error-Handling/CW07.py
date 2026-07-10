import logging

### Configuracion del logging: los mensajes se guardan en un archivo,
### con fecha, nivel de severidad y el mensaje
logging.basicConfig(
    filename="verifier_digit.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


### Excepcion personalizada para cuando el digito verificador no coincide.
### Guarda el rol y el digito esperado como datos extra, tal como se vio
### en la diapositiva "Adding Detail to Custom Exceptions"
class DigitoVerificadorError(Exception):
    def _init_(self, rol, esperado):
        self.rol = rol
        self.esperado = esperado
        super()._init_(f"El digito verificador de '{rol}' no coincide. Esperado: {esperado}")


# INPUT
### Pedimos el rol en un ciclo hasta que sea valido. Usamos try/except/else:
### el except atrapa errores de formato, el else solo corre si NO hubo error
rol_valido = False
while not rol_valido:
    try:
        rol = input("Ingrese el rol (formato: 12345-6): ")
        rol_sin_digito, digito = rol.split("-")

        if not rol_sin_digito.isnumeric():
            raise ValueError(f"'{rol_sin_digito}' tiene caracteres no numericos")
        if not digito.isnumeric():
            raise ValueError(f"'{digito}' no es un digito verificador valido")

    except ValueError as e:
        ### Aqui caen tanto el error del split (rol sin guion) como
        ### los errores de validacion que lanzamos nosotros mismos
        logging.warning(f"Rol invalido ingresado: {e}")
        print(f"Rol incorrecto: {e}")
    else:
        ### Solo llegamos aqui si el try no lanzo ninguna excepcion
        rol_valido = True


# PROCESS
### Invertimos el rol para aplicar el algoritmo del digito verificador
invertido = rol_sin_digito[::-1]

### Secuencia de multiplicadores que se repite cada 6 posiciones
secuencia = [2, 3, 4, 5, 6, 7]
suma = 0

for index in range(len(invertido)):
    multiplicando = secuencia[index % 6]
    numero = int(invertido[index:index + 1])
    suma += numero * multiplicando

total = suma % 11
verificador = 11 - total

### Caso especial del algoritmo: si el resultado da 11, el digito
### verificador correcto es 0
if verificador == 11:
    verificador = 0


# OUTPUT
### try/except/else/finally completo: else corre si el rol es correcto,
### finally corre siempre, haya o no error
try:
    if verificador != int(digito):
        raise DigitoVerificadorError(rol_sin_digito, verificador)
except DigitoVerificadorError as e:
    logging.error(str(e))
    print(e)
else:
    print(f"Rol valido: {rol_sin_digito}-{verificador}")
finally:
    print("Verificacion terminada.")