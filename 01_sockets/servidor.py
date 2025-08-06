# Servidor
import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP de localhost
PORT = 65432        # Puerto para la comunicación

# Crea un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Vincula el socket a la dirección y puerto
    s.bind((HOST, PORT))
    # Pone el socket a la escucha de conexiones (máximo 1 conexión en cola)
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    
    # Acepta una conexión entrante
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            # Recibe datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            
            mensaje_recibido = data.decode('utf-8')
            print(f"Mensaje del cliente: {mensaje_recibido}")
            
            # Envía una respuesta de vuelta al cliente
            mensaje_respuesta = f"Mensaje recibido: '{mensaje_recibido}'"
            conn.sendall(mensaje_respuesta.encode('utf-8'))
