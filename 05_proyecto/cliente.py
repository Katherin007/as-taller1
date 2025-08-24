# Cliente
import socket
import threading

# Definir el host y puerto
HOST = '127.0.0.1'
PORT = 65432

def recibir_mensajes(s):
    """Maneja la recepción de mensajes del servidor."""
    while True:
        try:
            mensaje = s.recv(1024).decode('utf-8')
            if mensaje:
                print(f"\n{mensaje}")
         # Si el servidor se cierra limpiamente, recv devuelve una cadena vacía.
            else:
                print("El servidor se ha desconectado o cerrado.")
                s.close()
                break
              # Captura el error si el servidor se cae abruptamente (WinError 10053)
        except ConnectionAbortedError:
            print("Conexión abortada por el servidor.")
            s.close()
            break
            
        # Captura cualquier otro error de socket
        except():
            print("Desconectado del servidor debido a un error.")
            s.close()
            break
        except():
            print("Desconectado del servidor.")
            break

def iniciar_cliente():
    """Configura e inicia el cliente."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado al servidor. Escribe 'salir' para terminar.")
        
        # Iniciar un hilo para recibir mensajes
        hilo_recibir = threading.Thread(target=recibir_mensajes, args=(s,))
        hilo_recibir.start()
        
        while True:
            # Enviar mensajes del usuario
            mensaje = input()
            if mensaje.lower() == 'salir':
                break
            s.sendall(mensaje.encode('utf-8'))
            
# Iniciar el cliente
if __name__ == "__main__":
    iniciar_cliente()
