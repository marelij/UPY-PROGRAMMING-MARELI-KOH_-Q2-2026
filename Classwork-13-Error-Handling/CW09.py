#Input
verbo = input("Ingrese verbo: ")
#Process
#Lista de pronombres
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
#Diccionario de terminacion de los verbos
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}
try:
    raiz = verbo[:-2]
    final = verbo[-2:]
    lista_de_terminaciones = terminaciones[final]
except KeyError:
    print("El verbo debe terminar en 'ar', 'er' o 'ir'")
    raise SystemExit
except IndexError:
    print("El verbo ingresado es demasiado corto")
    raise SystemExit
#OUTPUT
for index, pronombre in enumerate(pronombres):
    terminacion = lista_de_terminaciones[index]
    print(f"{pronombre} {raiz}{terminacion}")