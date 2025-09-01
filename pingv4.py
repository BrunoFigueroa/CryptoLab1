import sys
import time
from scapy.all import IP, ICMP, sr1, hexdump

# ----------------------------
# VALIDACIÓN DE ARGUMENTOS
# ----------------------------
if len(sys.argv) != 2:
    print('Se necesita el mensaje a enviar. ejemplo: "larycxpajorj h bnpdarmjm nw anmnb"')
    sys.exit(1)

mensaje = sys.argv[1]

# ----------------------------
# PING REAL (DEMO)
# ----------------------------
#print("\nEjemplo de paquete ICMP 'real':")
#ping_normal = IP(dst="8.8.8.8") / ICMP(type=8) / b"ping"
#ping_respuesta = sr1(ping_normal, timeout=2, verbose=0)
#ping_normal.show()
#print("Hexdump del paquete:")
#hexdump(ping_normal)

# ----------------------------
# ENVÍO DE MENSAJE EN ICMP (UNO POR CARÁCTER)
# ----------------------------

for i, caracter in enumerate(mensaje):
    # Generar padding con valores incrementales: 1, 2, 3, ..., 47
    padding = bytes((x % 256 for x in range(1, 48)))
    paquete = IP(dst="8.8.8.8") / ICMP(type=8) / (caracter.encode() + padding)
    respuesta = sr1(paquete, timeout=2, verbose=0)

    print(".")
    print("Sent 1 packets.")
    #paquete.show()
    #print("-" * 40)
    time.sleep(0.3)  # retraso

#print("\n✔ Todos los caracteres enviados.")
