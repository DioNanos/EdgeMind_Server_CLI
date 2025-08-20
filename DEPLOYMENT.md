<!-- ENGLISH -->
# Deployment Guide

This document provides detailed technical instructions for deploying the EdgeMind CLI Server.

## Prerequisites

-   [Docker](https://docs.docker.com/get-docker/) installed on your server machine.

## Quick Start

1.  **Clone or download this repository.**

2.  **Configure the API Key:**
    The server uses an API Key for security. You **must** change the default key. The key is passed to the Docker container as an environment variable. Choose a long, random string for your key.

3.  **Build the Docker Image:**
    Navigate to the root directory of this project (where the `Dockerfile` is) and run:
    ```bash
    docker build -t edgemind-cli-server .
    ```

4.  **Run the Docker Container:**
    Run the container, mapping a local port (e.g., `5000`) to the container's port `5000` and setting your secret API key.

    ```bash
    docker run -d -p 5000:5000 --name edgemind-server -e API_KEY="YOUR_SUPER_SECRET_API_KEY" edgemind-cli-server
    ```
    -   `-d`: Run the container in detached mode (in the background).
    -   `-p 5000:5000`: Map port 5000 on the host to port 5000 in the container.
    -   `--name edgemind-server`: Give the container a memorable name.
    -   `-e API_KEY="..."`: **This is where you set your secret API key.**

5.  **Verify it's running:**
    You can check the logs to make sure the server started correctly:
    ```bash
    docker logs edgemind-server
    ```

## API Endpoint

-   **URL:** `http://<your_server_ip>:5000/execute`
-   **Method:** `POST`
-   **Authentication Header:** `Authorization: Bearer <YOUR_SUPER_SECRET_API_KEY>`

## Production Considerations

-   **HTTPS:** The default Flask server does not use HTTPS. For production, you should run this server behind a reverse proxy like Nginx or Caddy that can handle SSL/TLS termination. This is critical for protecting your API key and data in transit.
-   **WSGI Server:** The Flask development server is not suitable for production. The Docker image should be modified to use a production-grade WSGI server like Gunicorn or uWSGI for better performance and stability.

---

<!-- ITALIANO -->
# Guida al Deployment

Questo documento fornisce istruzioni tecniche dettagliate per il deployment dell'EdgeMind CLI Server.

## Prerequisiti

-   [Docker](https://docs.docker.com/get-docker/) installato sulla tua macchina server.

## Avvio Rapido

1.  **Clona o scarica questo repository.**

2.  **Configura la API Key:**
    Il server utilizza una API Key per la sicurezza. **Devi** cambiare la chiave predefinita. La chiave viene passata al container Docker come variabile d'ambiente. Scegli una stringa lunga e casuale per la tua chiave.

3.  **Build dell'Immagine Docker:**
    Naviga nella directory principale di questo progetto (dove si trova il `Dockerfile`) ed esegui:
    ```bash
    docker build -t edgemind-cli-server .
    ```

4.  **Esegui il Container Docker:**
    Esegui il container, mappando una porta locale (es. `5000`) alla porta `5000` del container e impostando la tua API key segreta.

    ```bash
    docker run -d -p 5000:5000 --name edgemind-server -e API_KEY="TUA_API_KEY_SEGRETA" edgemind-cli-server
    ```
    -   `-d`: Esegue il container in modalità detached (in background).
    -   `-p 5000:5000`: Mappa la porta 5000 sull'host alla porta 5000 nel container.
    -   `--name edgemind-server`: Assegna un nome riconoscibile al container.
    -   `-e API_KEY="..."`: **Qui è dove imposti la tua API key segreta.**

5.  **Verifica che sia in esecuzione:**
    Puoi controllare i log per assicurarti che il server sia partito correttamente:
    ```bash
    docker logs edgemind-server
    ```

## Endpoint API

-   **URL:** `http://<ip_del_tuo_server>:5000/execute`
-   **Metodo:** `POST`
-   **Header di Autenticazione:** `Authorization: Bearer <TUA_API_KEY_SEGRETA>`

## Considerazioni per la Produzione

-   **HTTPS:** Il server di sviluppo di Flask non usa HTTPS. In produzione, dovresti eseguire questo server dietro un reverse proxy come Nginx o Caddy che possa gestire la terminazione SSL/TLS. Questo è fondamentale per proteggere la tua API key e i dati in transito.
-   **WSGI Server:** Il server di sviluppo di Flask non è adatto alla produzione. L'immagine Docker dovrebbe essere modificata per usare un server WSGI di livello produzione come Gunicorn o uWSGI per migliori performance e stabilità.

---

<!-- ESPAÑOL -->
# Guía de Despliegue

Este documento proporciona instrucciones técnicas detalladas para desplegar el EdgeMind CLI Server.

## Prerrequisitos

-   [Docker](https://docs.docker.com/get-docker/) instalado en tu máquina servidor.

## Inicio Rápido

1.  **Clona o descarga este repositorio.**

2.  **Configura la API Key:**
    El servidor utiliza una API Key por seguridad. **Debes** cambiar la clave predeterminada. La clave se pasa al contenedor de Docker como una variable de entorno. Elige una cadena larga y aleatoria para tu clave.

3.  **Construye la Imagen de Docker:**
    Navega al directorio raíz de este proyecto (donde se encuentra el `Dockerfile`) y ejecuta:
    ```bash
    docker build -t edgemind-cli-server .
    ```

4.  **Ejecuta el Contenedor de Docker:**
    Ejecuta el contenedor, mapeando un puerto local (p. ej., `5000`) al puerto `5000` del contenedor y estableciendo tu API key secreta.

    ```bash
    docker run -d -p 5000:5000 --name edgemind-server -e API_KEY="TU_API_KEY_SECRETA" edgemind-cli-server
    ```
    -   `-d`: Ejecuta el contenedor en modo detached (en segundo plano).
    -   `-p 5000:5000`: Mapea el puerto 5000 en el host al puerto 5000 en el contenedor.
    -   `--name edgemind-server`: Dale un nombre memorable al contenedor.
    -   `-e API_KEY="..."`: **Aquí es donde estableces tu API key secreta.**

5.  **Verifica que se está ejecutando:**
    Puedes revisar los logs para asegurarte de que el servidor se ha iniciado correctamente:
    ```bash
    docker logs edgemind-server
    ```

## Endpoint de la API

-   **URL:** `http://<ip_de_tu_servidor>:5000/execute`
-   **Método:** `POST`
-   **Cabecera de Autenticación:** `Authorization: Bearer <TU_API_KEY_SECRETA>`

## Consideraciones para Producción

-   **HTTPS:** El servidor de desarrollo de Flask no usa HTTPS. En producción, deberías ejecutar este servidor detrás de un proxy inverso como Nginx o Caddy que pueda manejar la terminación SSL/TLS. Esto es crítico para proteger tu API key y los datos en tránsito.
-   **Servidor WSGI:** El servidor de desarrollo de Flask no es adecuado para producción. La imagen de Docker debería ser modificada para usar un servidor WSGI de grado de producción como Gunicorn o uWSGI para un mejor rendimiento y estabilidad.
