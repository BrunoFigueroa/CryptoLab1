import sys

# Mandar el mensaje a encriptar y el desplazamiento. Ej:
# sudo python3 cesar.py "criptografia y seguridad en redes" 9
# larycxpajorj h bnpdanmjm nw anmnb

def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            ascii_offset = ord('a')
            # Convertimos a minúsculas para trabajar solo con letras minúsculas
            caracter = caracter.lower()
            posicion = ord(caracter) - ascii_offset
            nueva_posicion = (posicion + desplazamiento) % 26
            nuevo_caracter = chr(nueva_posicion + ascii_offset)
            mensaje_cifrado += nuevo_caracter
        else:
            mensaje_cifrado += caracter  # Mantiene espacios y otros caracteres
    return mensaje_cifrado

# Verificar argumentos desde la terminal
if len(sys.argv) != 3:
    print("Uso: sudo python3 cesar.py \"mensaje a cifrar\" desplazamiento")
    sys.exit(1)

mensaje = sys.argv[1]
try:
    desplazamiento = int(sys.argv[2])
except ValueError:
    print("Error: El desplazamiento debe ser un número entero.")
    sys.exit(1)

mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
print(mensaje_cifrado)
