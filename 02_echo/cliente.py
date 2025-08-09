# Cliente
import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

def iniciar_cliente_echo():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # Bucle para enviar mensajes
        while True:
            mensaje = input("Introduce un mensaje para enviar (o 'salir' para terminar): ")
            if mensaje.lower() == 'salir':
                break
            
            # Envía el mensaje codificado
            s.sendall(mensaje.encode('utf-8'))
            
            # Recibe la respuesta del servidor
            data = s.recv(1024)
            print(f"Mensaje enviado: '{mensaje}'")
            print(f"Respuesta del servidor: '{data.decode('utf-8')}'")
            print("-" * 20)

if __name__ == "__main__":
    iniciar_cliente_echo()

