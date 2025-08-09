# Servidor
import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

sockets_conectados = []

def manejar_cliente(cliente_socket):
    """Maneja la comunicación con un cliente específico."""
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if mensaje:
                print(f"Recibido: {mensaje}")
                # Retransmitir el mensaje a todos los demás clientes
                retransmitir_mensaje(mensaje, cliente_socket)
            else:
                # El cliente se desconectó
                eliminar_cliente(cliente_socket)
                break
        except:
            eliminar_cliente(cliente_socket)
            break

def retransmitir_mensaje(mensaje, remitente):
    """Envía un mensaje a todos los clientes excepto al remitente."""
    for socket_cliente in sockets_conectados:
        if socket_cliente != remitente:
            try:
                socket_cliente.send(mensaje.encode('utf-8'))
            except:
                socket_cliente.close()
                eliminar_cliente(socket_cliente)

def eliminar_cliente(cliente_socket):
    """Elimina un cliente de la lista de sockets conectados."""
    if cliente_socket in sockets_conectados:
        sockets_conectados.remove(cliente_socket)
        print("Un cliente se ha desconectado.")

def iniciar_servidor_chat():
    """Configura y inicia el servidor de chat."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor de chat escuchando en {HOST}:{PORT}")

    while True:
        cliente_socket, addr = server.accept()
        sockets_conectados.append(cliente_socket)
        print(f"Nuevo cliente conectado desde {addr}")
        
        # Iniciar un nuevo hilo para manejar este cliente
        thread = threading.Thread(target=manejar_cliente, args=(cliente_socket,))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor_chat()

