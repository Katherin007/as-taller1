# Cliente
import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor

# Crea un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta al servidor
    s.connect((HOST, PORT))
    print(f"Conectado al servidor en {HOST}:{PORT}")
    
    # Envía un mensaje al servidor
    mensaje_enviado = "¡Hola desde el cliente!"
    s.sendall(mensaje_enviado.encode('utf-8'))
    print(f"Enviado: {mensaje_enviado}")
    
    # Recibe la respuesta del servidor
    data = s.recv(1024)
    mensaje_recibido = data.decode('utf-8')
    print(f"Respuesta del servidor: {mensaje_recibido}")
