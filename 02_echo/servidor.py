# Servidor
import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

def iniciar_servidor_echo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor Echo escuchando en {HOST}:{PORT}")
        
        while True:
            # Espera una conexión
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    # Recibe datos del cliente
                    data = conn.recv(1024)
                    if not data:
                        # Si no hay datos, el cliente se desconectó
                        print(f"Desconectado de {addr}")
                        break
                    
                    # Devuelve los mismos datos recibidos (Echo)
                    conn.sendall(data)

if __name__ == "__main__":
    iniciar_servidor_echo()
