# Cliente
import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

def recibir_mensajes(cliente_socket):
    """Hilo para recibir mensajes del servidor."""
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if mensaje:
                print(mensaje)
            else:
                print("Se ha perdido la conexión con el servidor.")
                cliente_socket.close()
                break
        except:
            print("Ha ocurrido un error al recibir mensajes.")
            cliente_socket.close()
            break

def enviar_mensajes(cliente_socket):
    """Hilo para enviar mensajes al servidor."""
    while True:
        mensaje = input()
        if mensaje.lower() == 'salir':
            cliente_socket.close()
            break
        cliente_socket.send(mensaje.encode('utf-8'))

def iniciar_cliente_chat():
    """Configura e inicia el cliente de chat."""
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente_socket.connect((HOST, PORT))
        print("Conectado al servidor de chat. Escribe un mensaje ('salir' para terminar).")
        
        # Hilos para enviar y recibir mensajes simultáneamente
        hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
        hilo_enviar = threading.Thread(target=enviar_mensajes, args=(cliente_socket,))
        
        hilo_recibir.start()
        hilo_enviar.start()
        
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que está en ejecución.")

if __name__ == "__main__":
    iniciar_cliente_chat()


