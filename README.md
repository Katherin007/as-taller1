# taller #1 de Arquitectura de Software: Cliente-Servidor

## Descripción

Este proyecto proporciona una plantilla para la implementación de los ejemplos del modelo Cliente/Servidor, según se explican en el vídeo [Programando Cliente/Servidor con Python](https://www.youtube.com/watch?v=kPXa73a0kCA)

## Estructura del Proyecto

```
as-taller1/
├── README.md
├── requirements.txt
├── .gitignore
├── 01_sockets/
│   ├── cliente.py
│   └── servidor.py
├── 02_echo/
│   ├── cliente.py
│   └── servidor.py
├── 03_chat/
│   ├── cliente.py
│   └── servidor.py
├── 04_http/
│   ├── cliente.py
│   └── servidor.py
└── 05_proyecto/
    ├── cliente.py
    └── servidor.py
```

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/UR-CC/as-taller1.git
cd as-taller1

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual en Windows:
venv\Scripts\activate
# Activar entorno virtual en Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejercicios

### 1. Sockets Básicos (Paso de Mensajes)

- **Ubicación**: `01_sockets/`
- **Descripción**: Implementación básica de comunicación cliente-servidor con sockets
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py


 Este archivo implementa un servidor TCP básico en Python utilizando el módulo estándar socket. El servidor escucha conexiones entrantes en la dirección IP local (127.0.0.1) y el puerto 65432. Una vez que un cliente se conecta, el servidor recibe mensajes, los imprime y responde confirmando la recepción.

Descripción de las secciones principales
1. Configuración del servidor
HOST: IP donde el servidor escuchará (localhost).
PORT: Puerto TCP donde el servidor aceptará conexiones.
2. Creación y configuración del socket
Se crea un socket TCP (SOCK_STREAM) usando IPv4 (AF_INET).
El socket se vincula a la IP y puerto definidos.
El servidor se pone en modo escucha, esperando conexiones entrantes.
3. Aceptación de conexiones y comunicación 
El servidor acepta una conexión entrante.
Entra en un bucle donde:
Recibe datos del cliente.
Si no hay datos, termina la conexión.
Decodifica y muestra el mensaje recibido.
Envía una respuesta de confirmación al cliente.
Funcionamiento general
El servidor inicia y espera una conexión.
Cuando un cliente se conecta, el servidor recibe mensajes y responde.
El ciclo continúa hasta que el cliente cierra la conexión.
Uso
Ejecuta este script para iniciar el servidor.
Conéctate desde un cliente TCP (puede ser otro script o una herramienta como netcat).
Envía mensajes y observa las respuestas del servidor. 


# Terminal 2 - Cliente
python cliente.py
```

Este archivo implementa un cliente TCP en Python utilizando el módulo estándar socket. El cliente se conecta a un servidor en la dirección IP local (127.0.0.1) y el puerto 65432, envía un mensaje y espera una respuesta.

Descripción de las secciones principales
1. Configuración del cliente
HOST: IP del servidor al que se conectará el cliente (localhost).
PORT: Puerto TCP del servidor.
2. Creación y conexión del socket
Se crea un socket TCP (SOCK_STREAM) usando IPv4 (AF_INET).
El cliente se conecta al servidor usando la IP y el puerto definidos.
3. Envío y recepción de mensajes
El cliente envía un mensaje codificado en UTF-8 al servidor.
Espera y recibe la respuesta del servidor.
Decodifica la respuesta y la muestra por pantalla.
Funcionamiento general
El cliente se conecta al servidor.
Envía un mensaje de saludo.
Recibe y muestra la respuesta del servidor.
La conexión se cierra automáticamente al salir del bloque with.
Uso
Asegúrate de que el servidor esté en ejecución.
Ejecuta este script para conectar el cliente al servidor, enviar un mensaje y recibir la respuesta.

### 2. Servidor Echo

- **Ubicación**: `02_echo/`
- **Descripción**: Servidor que devuelve exactamente lo que recibe del cliente
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py
Este archivo implementa un servidor Echo TCP en Python usando el módulo estándar socket. El servidor escucha conexiones en la dirección IP local (127.0.0.1) y el puerto 65432. Por cada cliente conectado, el servidor recibe mensajes y responde enviando exactamente los mismos datos recibidos (funcionalidad "echo").

Descripción de las secciones principales
1. Configuración del servidor
HOST: IP donde el servidor escuchará (localhost).
PORT: Puerto TCP donde el servidor aceptará conexiones.
2. Función principal del servidor Echo
Se crea un socket TCP usando IPv4.
El socket se vincula a la IP y puerto definidos.
El servidor se pone en modo escucha para aceptar conexiones entrantes.
3. Manejo de conexiones y funcionalidad Echo
El servidor acepta conexiones de clientes en un bucle infinito.
Por cada cliente:
Recibe datos.
Si no hay datos, el cliente se desconectó.
Si hay datos, los reenvía tal cual al cliente (echo).
4. Ejecución del servidor
Permite ejecutar el servidor directamente desde la línea de comandos.
Funcionamiento general
El servidor inicia y espera conexiones.
Cuando un cliente se conecta, el servidor recibe mensajes y responde con los mismos datos.
El ciclo continúa hasta que el cliente se desconecta.
Uso
Ejecuta este script para iniciar el servidor Echo.
Conéctate desde un cliente TCP (otro script o herramienta como netcat).
Envía mensajes y observa que el servidor responde con el mismo contenido.

# Terminal 2 - Cliente
python cliente.py
```
Este archivo implementa un cliente TCP Echo en Python usando el módulo estándar socket. El cliente se conecta a un servidor Echo en la dirección IP local (127.0.0.1) y el puerto 65432. Permite al usuario enviar mensajes al servidor y muestra la respuesta recibida (que debe ser el mismo mensaje enviado).

Descripción de las secciones principales
1. Configuración del servidor
HOST: IP del servidor al que se conectará el cliente (localhost).
PORT: Puerto TCP del servidor.
2. Función principal del cliente Echo
Se crea un socket TCP usando IPv4.
El cliente se conecta al servidor usando la IP y el puerto definidos.
3. Envío y recepción de mensajes
El usuario introduce un mensaje por teclado.
Si el mensaje es 'salir', el cliente termina.
El mensaje se envía al servidor codificado en UTF-8.
El cliente recibe la respuesta del servidor y la muestra por pantalla.
4. Ejecución del cliente
Permite ejecutar el cliente directamente desde la línea de comandos.
Funcionamiento general
El cliente se conecta al servidor Echo.
El usuario puede enviar mensajes y recibe como respuesta el mismo mensaje enviado.
El ciclo continúa hasta que el usuario escribe 'salir'.
Uso
Asegúrate de que el servidor Echo esté en ejecución.
Ejecuta este script para iniciar el cliente.
Escribe mensajes para enviarlos al servidor y ver la respuesta.
Escribe 'salir' para terminar la conexión.


### 3. Chat Multiusuario

- **Ubicación**: `03_chat/`
- **Descripción**: Sistema de chat que permite múltiples usuarios conectados simultáneamente
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py

Este archivo implementa un servidor de chat multiusuario en Python usando sockets y multithreading. Permite que varios clientes se conecten simultáneamente y que los mensajes enviados por un cliente sean retransmitidos a todos los demás clientes conectados.

Componentes principales
1. Configuración del servidor
HOST: IP donde el servidor escuchará (localhost).
PORT: Puerto TCP donde el servidor aceptará conexiones.
2. Lista de clientes conectados
Lista global que almacena los sockets de todos los clientes actualmente conectados.
3. Función manejar_cliente
Atiende a un cliente específico en un hilo independiente.
Recibe mensajes del cliente y los retransmite a los demás.
Si el cliente se desconecta o ocurre un error, lo elimina de la lista de clientes conectados.
4. Función retransmitir_mensaje
Envía el mensaje recibido a todos los clientes conectados excepto al remitente.
Si ocurre un error al enviar, elimina el cliente problemático.
5. Función eliminar_cliente
Elimina el socket del cliente de la lista global y muestra un mensaje en consola.
6. Función iniciar_servidor_chat
Crea el socket del servidor, lo vincula y lo pone en escucha.
Acepta conexiones entrantes en un bucle infinito.
Por cada nuevo cliente, crea un hilo para manejar su comunicación.
7. Ejecución principal
Permite ejecutar el servidor directamente desde la línea de comandos.
Funcionamiento general
El servidor inicia y espera conexiones de clientes.
Cada cliente conectado puede enviar mensajes.
Los mensajes se retransmiten a todos los demás clientes conectados.
Si un cliente se desconecta, se elimina de la lista de clientes activos.
Uso
Ejecuta este script para iniciar el servidor de chat.
Conéctate desde varios clientes (usando el cliente correspondiente).
Los mensajes enviados por un cliente serán recibidos por todos los demás.


# Terminales adicionales - Clientes
python cliente.py
```
Este archivo implementa un cliente TCP Echo en Python usando el módulo estándar socket. El cliente se conecta a un servidor Echo en la dirección IP local (127.0.0.1) y el puerto 65432. Permite al usuario enviar mensajes al servidor y muestra la respuesta recibida (que debe ser el mismo mensaje enviado).

Descripción de las secciones principales
1. Configuración del servidor
HOST: IP del servidor al que se conectará el cliente (localhost).
PORT: Puerto TCP del servidor.
2. Función principal del cliente Echo
Se crea un socket TCP usando IPv4.
El cliente se conecta al servidor usando la IP y el puerto definidos.
3. Envío y recepción de mensajes
El usuario introduce un mensaje por teclado.
Si el mensaje es 'salir', el cliente termina.
El mensaje se envía al servidor codificado en UTF-8.
El cliente recibe la respuesta del servidor y la muestra por pantalla.
4. Ejecución del cliente
Permite ejecutar el cliente directamente desde la línea de comandos.

Funcionamiento general
El cliente se conecta al servidor Echo.
El usuario puede enviar mensajes y recibe como respuesta el mismo mensaje enviado.
El ciclo continúa hasta que el usuario escribe 'salir'.

Uso
Asegúrate de que el servidor Echo esté en ejecución.
Ejecuta este script para iniciar el cliente.
Escribe mensajes para enviarlos al servidor y ver la respuesta.
Escribe 'salir' para terminar la conexión.

### 4. Servidor HTTP Básico

- **Ubicación**: `04_http/`
- **Descripción**: Implementación de un servidor HTTP básico desde cero
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Servidor HTTP
python server.py

# Acceder desde navegador:
# http://localhost:8080
```
Este archivo implementa un servidor HTTP básico en Python utilizando sockets. El servidor escucha en la dirección IP local (127.0.0.1) y el puerto 8080, responde a las solicitudes HTTP entrantes y envía una página HTML simple como respuesta.

Componentes principales
1. Configuración del servidor
HOST: IP donde el servidor escuchará (localhost).
PORT: Puerto TCP donde el servidor aceptará conexiones HTTP.
2. Función generar_respuesta_http
Construye una respuesta HTTP completa, incluyendo cabeceras y el cuerpo HTML.
Define el código de estado, tipo de contenido, longitud y cierre de conexión.
3. Función iniciar_servidor_http
Crea el socket del servidor, lo vincula y lo pone en escucha.
Acepta conexiones entrantes en un bucle infinito.
Por cada conexión:
Recibe la petición HTTP del cliente.
Imprime la primera línea de la petición (por ejemplo, GET / HTTP/1.1).
Construye una página HTML simple.
Genera y envía la respuesta HTTP completa al cliente.
Cierra la conexión.
4. Ejecución principal
Permite ejecutar el servidor directamente desde la línea de comandos.

Funcionamiento general
El servidor inicia y espera conexiones HTTP.
Cuando un navegador o cliente realiza una petición, el servidor responde con una página HTML.
La conexión se cierra después de enviar la respuesta.

Uso
Ejecuta este script para iniciar el servidor HTTP.
Abre un navegador y accede a http://127.0.0.1:8080.
Verás una página web generada por el servidor Python.

### 5. Proyecto del Estudiante

- **Ubicación**: `05_proyecto/`
- **Descripción**: _Cada estudiante debe crear un programa cliente/servidor de su elección_
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py
Este archivo implementa un servidor de chat multiusuario en Python utilizando sockets y multithreading. Permite que varios clientes se conecten simultáneamente y que los mensajes enviados por un cliente sean retransmitidos a todos los demás clientes conectados.

Componentes principales
1. Configuración del servidor
HOST: IP donde el servidor escuchará (localhost).
PORT: Puerto TCP donde el servidor aceptará conexiones.
2. Lista de clientes conectados
Lista global que almacena los sockets de todos los clientes actualmente conectados.
3. Función manejar_cliente
Atiende a un cliente específico en un hilo independiente.
Recibe mensajes del cliente y los retransmite a los demás clientes conectados.
Si el cliente se desconecta o ocurre un error, lo elimina de la lista de clientes conectados y cierra la conexión.
4. Función iniciar_servidor
Crea el socket del servidor, lo vincula y lo pone en escucha.
Acepta conexiones entrantes en un bucle infinito.
Por cada nuevo cliente, crea un hilo para manejar su comunicación.
5. Ejecución principal
Permite ejecutar el servidor directamente desde la línea de comandos.
Funcionamiento general
El servidor inicia y espera conexiones de clientes.
Cada cliente conectado puede enviar mensajes.
Los mensajes se retransmiten a todos los demás clientes conectados.
Si un cliente se desconecta, se elimina de la lista de clientes activos y se cierra su socket.
Uso
Ejecuta este script para iniciar el servidor de chat.
Conéctate desde varios clientes (usando el cliente correspondiente).
Los mensajes enviados por un cliente serán recibidos por todos los demás.

# Terminal 2 - Cliente
python cliente.py
```
Este archivo implementa un cliente de chat multiusuario en Python utilizando sockets y multithreading. Permite conectarse a un servidor de chat, enviar mensajes y recibir mensajes de otros usuarios en tiempo real.

Componentes principales
1. Configuración del cliente
HOST: IP del servidor al que se conectará el cliente (localhost).
PORT: Puerto TCP del servidor.
2. Función recibir_mensajes
Se ejecuta en un hilo independiente.
Recibe mensajes del servidor y los muestra por pantalla.
Si el servidor se desconecta o ocurre un error, cierra el socket y termina el hilo.
3. Función iniciar_cliente
Crea el socket del cliente y se conecta al servidor.
Inicia un hilo para recibir mensajes del servidor.
Permite al usuario enviar mensajes desde la consola.
Si el usuario escribe 'salir', termina la conexión.
4. Ejecución principal
Permite ejecutar el cliente directamente desde la línea de comandos.

Funcionamiento general
El cliente se conecta al servidor de chat.
El usuario puede escribir mensajes que serán enviados al servidor.
Los mensajes de otros usuarios se reciben y se muestran automáticamente.
Si el usuario escribe 'salir' o el servidor se desconecta, la conexión se cierra.

Uso
Asegúrate de que el servidor de chat esté en ejecución.
Ejecuta este script para iniciar el cliente.
Escribe mensajes para enviarlos al chat.
Escribe 'salir' para terminar la conexión.


## Conceptos

#### Modelo Cliente/Servidor

Esta arquitectura es un patrón de diseño de software en el que las tareas se dividen entre los **proveedores de un recurso o servicio** (servidores) y los **solicitantes** de dicho servicio (clientes).

* **El Servidor:** Es un programa que se ejecuta de forma continua, esperando y escuchando solicitudes de los clientes. Puede manejar una o múltiples conexiones, como en el caso del chat multiusuario. Sus responsabilidades incluyen:
   * Gestionar el acceso a recursos compartidos (como la base de datos de un sitio web o los mensajes de un chat).
   * Responder a las solicitudes de los clientes.
   * Autenticar usuarios.

* **El Cliente:** Es un programa que inicia la comunicación y envía solicitudes al servidor. Sus responsabilidades son:
   * Interactuar con el usuario.
   * Enviar solicitudes bien formadas al servidor.
   * Procesar y mostrar la respuesta del servidor.

**Patrones de Interacción:**

* **Modelo de Petición/Respuesta (Request/Response):** Es el patrón más simple. El cliente envía una solicitud al servidor y espera una respuesta antes de hacer otra cosa. El servidor procesa la solicitud y envía la respuesta. El ejemplo del **Servidor Echo** y el **Servidor HTTP Básico** se basan directamente en este patrón.

* **Modelo de Publicador/Suscriptor (Publisher/Subscriber):** En este patrón, el servidor actúa como un "publicador" que envía mensajes a los clientes que se han "suscrito" a un tema de interés. El **Chat Multiusuario** es un ejemplo de este patrón, donde los mensajes de un usuario se "publican" a todos los demás clientes "suscritos" al chat.

#### Red de Computadores

Es un conjunto de equipos y dispositivos interconectados que comparten recursos e información. La conexión puede ser física (como un cable Ethernet) o inalámbrica (Wi-Fi). Los conceptos de **cliente** y **servidor** son fundamentales en este contexto:

  * **Cliente:** Una aplicación que inicia una solicitud a otra computadora (el servidor).
  * **Servidor:** Una aplicación que escucha las solicitudes entrantes y responde a ellas.

#### Protocolos de Red

Es un conjunto de reglas que definen cómo los datos deben ser formateados, transmitidos y recibidos. Para que el cliente y el servidor se entiendan, necesitan hablar el mismo "idioma". Ese idioma es un protocolo. En este proyecto, los protocolos más relevantes son **TCP** y **HTTP**.

   * **TCP (Transmission Control Protocol):** Es un protocolo de transporte que garantiza una comunicación fiable, ordenada y orientada a la conexión. Esto significa que antes de enviar datos, el cliente y el servidor establecen una conexión y, una vez que los datos se envían, TCP verifica que llegaron correctamente y en el orden adecuado. Es ideal para aplicaciones donde no se pueden perder datos, como un chat o la transferencia de archivos.

   * **HTTP (Hypertext Transfer Protocol):** Es un protocolo de aplicación diseñado para la comunicación entre navegadores web (clientes) y servidores web. Se basa en TCP y define cómo los navegadores solicitan páginas web y cómo los servidores responden. En el proyecto, el **Servidor HTTP Básico** implementa una versión simple de este protocolo.

#### Sockets

Es un **punto final** de comunicación en una red. Piensa en un socket como un extremo de una tubería. Cuando un cliente y un servidor se conectan, crean una "tubería" (la conexión) entre sus respectivos sockets para intercambiar datos. En Python, la librería `socket` proporciona las funciones para crear y manipular estos puntos de conexión.

**Proceso Básico del Servidor**:

* `socket()`: Crea un nuevo socket.
* `bind()`: Asocia el socket a una dirección IP y un número de puerto específicos. Esto le dice al sistema operativo que este servidor "escucha" en esa dirección.
* `listen()`: Pone el socket en modo de escucha para aceptar conexiones entrantes.
* `accept()`: Bloquea la ejecución y espera una conexión de un cliente. Cuando llega una conexión, devuelve un nuevo socket para esa conexión específica y la dirección del cliente.

**Proceso Básico del Cliente**:

* `socket()`: Crea un nuevo socket.
* `connect()`: Se conecta al socket del servidor especificado por su dirección IP y puerto.

Los sockers pueden ser creados sobre protocolo TCP o UDP, su elección depende de la necesidad de fiabilidad versus velocidad.

**Sockets TCP (Orientados a la Conexión)**:

* **Características**:

    * **Fiabilidad:** Garantiza que los paquetes de datos lleguen en el orden correcto y sin errores. Si se pierde un paquete, TCP lo reenvía.
    * **Orientación a la conexión:** Establece una conexión persistente (el "handshake" de tres vías) antes de enviar datos y la cierra al finalizar.
    * **Control de flujo:** Evita que un emisor rápido sature a un receptor lento.

* **Casos de uso:** Aplicaciones donde la integridad de los datos es crítica:

    * Navegación web (HTTP).
    * Transferencia de archivos (FTP).
    * Correo electrónico.
    * Chat multiusuario, como el del proyecto, para asegurar que todos los mensajes se entregan.

**Sockets UDP (Sin Conexión)**

* **Características:**

    * **No fiable:** Los paquetes (llamados datagramas) se envían sin establecer una conexión previa. No hay garantía de que lleguen, ni de que lo hagan en el orden correcto.
    * **Sin conexión:** No hay "handshake". El emisor simplemente envía los datos.
    * **Velocidad:** Al no tener la sobrecarga de la fiabilidad, UDP es mucho más rápido.

* **Casos de uso:** Aplicaciones donde la velocidad es más importante que la fiabilidad: 

    * Streaming de video y audio en tiempo real.
    * Videojuegos en línea.
    * Consultas DNS (Domain Name System).

#### Programación Concurrente

Es la capacidad de un sistema para manejar múltiples tareas aparentemente al mismo tiempo. En lugar de procesar a un cliente por completo antes de atender al siguiente, la programación concurrente permite que el servidor alterne entre las conexiones de forma eficiente.

* **Threading (Hilos):** Los hilos son una de las formas más comunes de lograr la concurrencia en Python. Un **hilo** es una unidad de ejecución ligera dentro de un proceso. Para el chat multiusuario, el servidor puede crear un nuevo hilo por cada cliente que se conecta. Cada hilo se encarga de manejar la comunicación con su cliente específico, permitiendo que el hilo principal del servidor siga escuchando nuevas conexiones.

#### Puertos

Son un número de 16 bits que identifica una aplicación o servicio específico en una computadora. Cuando un cliente se conecta a una dirección IP, también debe especificar un puerto para que el sistema operativo sepa a qué programa entregar los datos. Por ejemplo, el puerto 80 es el puerto estándar para el tráfico HTTP. El proyecto **Servidor HTTP Básico** usará el puerto 80 (o un puerto similar) para recibir las solicitudes web.

## Sugerencias para aprender más ...

- Logging configurable por módulo
- Pruebas unitarias para cada ejemplo
- Documentación detallada por componente
- Manejo robusto de errores y excepciones
- Código limpio y bien documentado
- Patrones de diseño aplicados

## Recursos Adicionales

- [Documentación oficial de sockets en Python](https://docs.python.org/3/library/socket.html)
- [Python Socket Programming: Server and Client Example Guide](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
- [Python Socket Programming: Server-Client Connection](https://www.pubnub.com/blog/python-socket-programming-client-server/)
- [Guía completa de programación de sockets en Python](https://www.datacamp.com/es/tutorial/a-complete-guide-to-socket-programming-in-python)


