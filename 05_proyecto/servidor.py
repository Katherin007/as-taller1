# Servidor
import socket
import threading

# Definir el host y puerto
HOST = '127.0.0.1'  # localhost
PORT = 65432

# Lista para guardar los clientes conectados
clientes = []

def manejar_cliente(conn, addr):
    """Maneja la conexión con un cliente específico."""
    print(f"Conectado a {addr}")
    clientes.append(conn)
    
    while True:
        try:
            # Recibir datos del cliente
            mensaje = conn.recv(1024).decode('utf-8')
            
            # **Importante: Si el recv devuelve 0 bytes, el cliente cerró normalmente.**
            if not mensaje:
                break # Sale del bucle para cerrar la conexión
            
            # Reenviar el mensaje a todos los otros clientes
            for cliente in clientes:
                if cliente != conn:
                    # Incluimos un bloque try/except aquí por si un cliente se cae al enviar.
                    try:
                         cliente.sendall(mensaje.encode('utf-8'))
                    except():
                        # Si falla el envío, ese cliente debe ser manejado en otro hilo.
                        pass
                        
        # Capturamos el ConnectionResetError (u otros errores de socket)
        except ConnectionResetError:
             print(f"ERROR: Conexión perdida con {addr}")
             break # Sale del bucle para cerrar la conexión
        except Exception as e:
             # Para cualquier otro error inesperado.
             print(f"Un error inesperado ocurrió con {addr}: {e}")
             break

    # **Ejecutar siempre al salir del bucle:**
    print(f"Desconectado de {addr}")
    if conn in clientes:
        clientes.remove(conn)
    conn.close()

def iniciar_servidor():
    """Configura e inicia el servidor."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Enlazar el socket al host y puerto
        s.bind((HOST, PORT))
        s.listen()
        
        print(f"Servidor de chat iniciado en {HOST}:{PORT}")
        
        while True:
            # Esperar por una nueva conexión de un cliente
            conn, addr = s.accept()
            
            # Iniciar un nuevo hilo para manejar al cliente
            hilo_cliente = threading.Thread(target=manejar_cliente, args=(conn, addr))
            hilo_cliente.start()

# Iniciar el servidor
if __name__ == "__main__":
    iniciar_servidor()
