# Servidor
import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 8080

def generar_respuesta_http(body):
    """
    Construye una respuesta HTTP completa.
    """
    headers = "HTTP/1.1 200 OK\r\n"
    headers += "Content-Type: text/html; charset=utf-8\r\n"
    headers += "Content-Length: " + str(len(body.encode('utf-8'))) + "\r\n"
    headers += "Connection: close\r\n"
    headers += "\r\n" # Línea en blanco para separar cabeceras del cuerpo
    
    return (headers + body).encode('utf-8')

def iniciar_servidor_http():
    """
    Inicia el servidor HTTP y gestiona las conexiones.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor HTTP escuchando en http://{HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Conexión desde {addr}")
                
                # Recibe la petición del cliente
                peticion = conn.recv(1024).decode('utf-8')
                
                if peticion:
                    print("Petición recibida:\n", peticion.splitlines()[0])
                    
                    # Contenido de la página HTML
                    html_content = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="UTF-8">
                        <title>Servidor HTTP Básico</title>
                        <style>
                            body { font-family: sans-serif; text-align: center; margin-top: 50px; }
                            h1 { color: #333; }
                        </style>
                    </head>
                    <body>
                        <h1>¡Hola desde mi servidor HTTP!</h1>
                        <p>Esta página ha sido servida por un servidor web implementado con sockets en Python.</p>
                    </body>
                    </html>
                    """
                    
                    # Envía la respuesta HTTP completa
                    respuesta = generar_respuesta_http(html_content)
                    conn.sendall(respuesta)
                
                print("Conexión cerrada.")

if __name__ == "__main__":
    iniciar_servidor_http()

