def calcular_digito_verificador(rol):
    rol_str = str(rol)
    rol_invertido = rol_str[::-1]
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    
    for i, digito in enumerate(rol_invertido):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador
        modulo = suma % 11
    resultado = 11 - modulo
    return str(resultado)
def main():
    print("=== Calculadora de Dígito Verificador ===")
    rol_input = input("Ingresa tu rol: ")
    digito = calcular_digito_verificador(rol_input)
    print(f"Dígito verificador: {digito}")
    print(f"Rol completo: {rol_input}-{digito}")

if __name__ == "__main__":
    main()