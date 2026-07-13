config = {}

# INPUT - open and read the configuration file
try:
    archivo = open("config.txt", 'r')
except FileNotFoundError:
    print("Error: 'config.txt' not found. Make sure it is in the same folder.")
    exit()

# PROCESS - parse each "key=value" line into the config dictionary
try:
    for linea in archivo:
        clave, valor = linea.strip().split("=")
        config[clave] = float(valor)
except ValueError:
    print("Error: 'config.txt' has an invalid line (expected format key=value).")
    archivo.close()
    exit()
finally:
    archivo.close()

# PROCESO - parsear los enteros
try:
    ancho, alto, max_iter = int(config["ancho"]), int(config["alto"]), int(config["max_iter"])
except KeyError as e:
    print(f"Error: missing key {e} in 'config.txt'.")
    exit()

# OUTPUT - create the CSV file that will hold the results
try:
    salida = open("clase.csv", 'w')
except OSError:
    print("Error: could not create 'clase.csv'.")
    exit()

salida.write("fila, clumna, iteraciones\n")

# PROCESS - for every pixel, map it to a complex number and
# count how many iterations it takes to escape the Mandelbrot set
try:
    for fila in range(alto):
        for columna in range(ancho):
            real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)

            z = 0 + 0j
            iteraciones = 0

            while (abs(z) <= 2) and (iteraciones < max_iter):
                z = z * z + c
                iteraciones += 1

            # OUTPUT - write one row per grid point
            salida.write(f"{fila},{columna},{iteraciones}\n")

except KeyError as e:
    print(f"Error: missing key {e} in 'config.txt'.")

except ZeroDivisionError:
    print("Error: 'ancho' or 'alto' cannot be zero.")

except Exception as e:
    print(f"Unexpected error while computing the Mandelbrot set: {e}")

# OUTPUT - close the CSV file no matter what happened above
finally:
    salida.close()

print("DONE")