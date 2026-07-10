class DigitoVerificadorError(Exception):
    pass
check=True
while check:
    try:
        rol = input("Ingrese el rol: ")
        rol_sin_digito, digito = rol.split("-")
        check=False
    except ValueError:
        print("Rol incorrecto: No tiene el formato XXXXXXXXX-X")
else:
    try:
        digito=int(digito)
    except ValueError:
        print("El digito verificador debe ser numerico")
    else:
        try:
            rol_invertido=[int(i)for i in rol_sin_digito]
        except ValueError:
            print("Los digitos del rol deben ser numericos")
        else:
            rol_invertido.reverse()
            secuencia =[2,3,4,5,6,7]
            suma=0
            for index in range (len(rol_invertido)):
                multiplicando=secuencia[index % 6]
                numero = rol_invertido[index]
                suma+=numero * multiplicando
    
            total=suma%11
            verificador= 11- total
            try:
                if verificador != int(digito):
                    raise DigitoVerificadorError(f"El digito verificado no coincide, {verificador}")
            except DigitoVerificadorError as e:
                print(e)
            else:
                print(f"{rol_sin_digito}-{verificador}")