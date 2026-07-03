config = {}

#INPUT
archivo = open("config.txt", 'r')

#PROCESO
for linea in archivo:
    clave, valor = linea.strip().split("=")
    config[clave] = float(valor)
archivo.close()

#PROCESO - parsear los enteros
ancho, alto, max_iter = int(config["ancho"]), int(config["alto"]), int(config["max_iter"])

#OUTPUT
salida = open("clase.csv", 'w')
salida.write("fila, clumna, iteraciones\n")

#PROCESO
for fila in range(alto):
    for columna in range(ancho):
        real = config["real_min"] + (columna / ancho) * (config["real_max"]-config["real_min"])
        imag = config["imag_min"] + (fila / alto) * (config["imag_max"]-config["imag_min"])
        c = complex(real, imag)
        
        z = 0  + 0j
        iteraciones = 0
        
        while (abs(z) <= 2) and (iteraciones < max_iter):
            z = z * z + c
            iteraciones += 1
        
        #OUTPUT
        salida.write(f"{fila},{columna},{iteraciones}\n")
        
#OUTPUT
salida.close()
print("DONE")