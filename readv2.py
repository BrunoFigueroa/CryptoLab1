import sys
from scapy.all import rdpcap, IP, ICMP, Raw

def descifrar_cesar(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            ascii_offset = ord('a')
            posicion = ord(caracter.lower()) - ascii_offset
            nueva_posicion = (posicion - desplazamiento) % 26
            nuevo_caracter = chr(nueva_posicion + ascii_offset)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

if len(sys.argv) != 2:
    print("Uso: python3 descifrar_cesar.py archivo.pcapng")
    sys.exit(1)

pcap_file = sys.argv[1]
packets = rdpcap(pcap_file)

mensaje = ""
for pkt in packets:
    if IP in pkt and ICMP in pkt and Raw in pkt:
        if pkt[IP].src == "192.168.1.166" and pkt[IP].dst == "8.8.8.8":
            mensaje += chr(pkt[Raw].load[0])

for d in range(26):
    texto = descifrar_cesar(mensaje, d)
    if d == 9:  # forzar resaltado en corrimiento 9
        print(f"\033[92m{d}:		{texto}\033[0m")
    else:
        print(f"{d}:		{texto}")
