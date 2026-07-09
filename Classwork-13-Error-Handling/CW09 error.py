import logging

### Configuracion del logging: los mensajes se guardan en un archivo,
### con fecha, nivel de severidad y el mensaje
logging.basicConfig(
    filename="spanish_verb_conjugator.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


### Excepcion personalizada para cuando el verbo no termina en ar, er o ir.
### Guarda el verbo y la terminacion como datos extra, tal como se vio en
### la diapositiva "Adding Detail to Custom Exceptions"
class TerminacionInvalidaError(Exception):
    def _init_(self, verbo, terminacion):
        self.verbo = verbo
        self.terminacion = terminacion
        super()._init_(f"'{verbo}' termina en '{terminacion}', no en ar, er o ir")


# INPUT
### Estructuras requeridas por la instruccion: una lista para los pronombres
### y un diccionario donde la llave es la terminacion (ar/er/ir) y el valor
### es la lista de las 6 terminaciones, en el mismo orden que pronombres
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

### Pedimos el verbo en un ciclo hasta que sea valido. else solo corre si
### el try no lanzo ninguna excepcion
verbo_valido = False
while not verbo_valido:
    try:
        verbo = input("Ingrese verbo: ").strip().lower()

        if len(verbo) < 3:
            raise ValueError(f"'{verbo}' es demasiado corto para ser un verbo")
        if not verbo.isalpha():
            raise ValueError(f"'{verbo}' contiene caracteres no validos")

        terminacion = verbo[-2:]
        if terminacion not in terminaciones:
            raise TerminacionInvalidaError(verbo, terminacion)

    except ValueError as e:
        logging.warning(f"Verbo invalido: {e}")
        print(f"Verbo incorrecto: {e}")
    except TerminacionInvalidaError as e:
        logging.error(str(e))
        print(f"Verbo incorrecto: {e}")
    else:
        verbo_valido = True


# PROCESS
### Separamos la raiz del verbo (todo menos las ultimas 2 letras)
raiz = verbo[:-2]

### Usamos la terminacion como llave para obtener las 6 terminaciones correctas
terminaciones_correctas = terminaciones[terminacion]


# OUTPUT
### Recorremos cada pronombre junto con su terminacion correspondiente,
### usando el mismo indice en ambas listas (tal como pide la instruccion)
for i, pronombre in enumerate(pronombres):
    print(pronombre, raiz + terminaciones_correctas[i])