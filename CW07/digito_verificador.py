def calcular_digito_verificador(rol):
    # Convert rol to string
    rol_str = str(rol)
    # Reverse the number
    rol_invertido = rol_str[::-1]
    
    # Define the sequence
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    
    # Multiply each digit by the sequence
    for i, digito in enumerate(rol_invertido):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador
    
    # Modulo 11 and subtraction
    modulo = suma % 11
    resultado = 11 - modulo
    return str(resultado)

def main():
    # Ask user for rol
    rol_input = input("Enter your rol: ")
    digito = calcular_digito_verificador(rol_input)
    # Display result
    print(f"Verification digit: {digito}")
    print(f"Complete rol: {rol_input}-{digito}")

if __name__ == "__main__":
    main()