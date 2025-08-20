<!-- ENGLISH -->
# EdgeMind Server CLI

This repository contains the code for the official backend server of the [EdgeMind](https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind) Android application.

## What Is It For?

This server acts as a powerful and flexible bridge between the EdgeMind app and any command-line interface (CLI) AI tool. It allows the app to leverage the computing power of an external server and interact with tools like Gemini, Claude, Aider, and others, right from the palm of your hand.

Through this server, the EdgeMind app can:
- Securely execute commands on a remote server.
- Maintain interactive and contextual chat sessions.
- Interact with a filesystem, allowing the CLI to read and write files for complex tasks like code analysis and modification.

## How It Works

The architecture is simple and robust:

1.  The EdgeMind app sends a secure request (authenticated with an API Key) to this server.
2.  The server receives the request and starts or resumes a session with the specified CLI (e.g., `gemini chat`).
3.  The user's message is passed to the CLI.
4.  The CLI's response is captured and sent back to the EdgeMind app, which displays it to the user.

## Installation

Detailed technical instructions for installing and configuring the server via Docker can be found in the [DEPLOYMENT.md](DEPLOYMENT.md) file.

---

*Download the EdgeMind app from the Google Play Store:*
[https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind](https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind)

---

<!-- ITALIANO -->
# EdgeMind Server CLI

Questo repository contiene il codice per il server backend ufficiale dell'applicazione Android [EdgeMind](https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind).

## A Cosa Serve?

Questo server agisce come un ponte potente e flessibile tra l'app EdgeMind e qualsiasi strumento di intelligenza artificiale a riga di comando (CLI). Permette all'app di sfruttare la potenza di calcolo di un server esterno e di interagire con strumenti come Gemini, Claude, Aider e altri, direttamente dal palmo della tua mano.

L'app EdgeMind, tramite questo server, può:
- Eseguire comandi su un server remoto in modo sicuro.
- Mantenere sessioni di chat interattive e contestuali.
- Interagire con un filesystem, permettendo al CLI di leggere e scrivere file per compiti complessi come l'analisi e la modifica del codice.

## Come Funziona

L'architettura è semplice e robusta:

1.  L'app EdgeMind invia una richiesta sicura (autenticata con API Key) a questo server.
2.  Il server riceve la richiesta e avvia o riprende una sessione con il CLI specificato (es. `gemini chat`).
3.  Il messaggio dell'utente viene passato al CLI.
4.  La risposta del CLI viene catturata e rispedita all'app EdgeMind, che la mostra all'utente.

## Installazione

Le istruzioni tecniche dettagliate per l'installazione e la configurazione del server tramite Docker si trovano nel file [DEPLOYMENT.md](DEPLOYMENT.md).

---

*Scarica l'app EdgeMind dal Google Play Store:*
[https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind](https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind)

---

<!-- ESPAÑOL -->
# EdgeMind Server CLI

Este repositorio contiene el código del servidor backend oficial para la aplicación Android [EdgeMind](https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind).

## ¿Para qué sirve?

Este servidor actúa como un puente potente y flexible entre la app EdgeMind y cualquier herramienta de inteligencia artificial de línea de comandos (CLI). Permite a la app aprovechar la potencia de cálculo de un servidor externo e interactuar con herramientas como Gemini, Claude, Aider y otras, directamente desde la palma de tu mano.

A través de este servidor, la app EdgeMind puede:
- Ejecutar comandos de forma segura en un servidor remoto.
- Mantener sesiones de chat interactivas y contextuales.
- Interactuar con un sistema de archivos, permitiendo al CLI leer y escribir archivos para tareas complejas como el análisis y la modificación de código.

## ¿Cómo funciona?

La arquitectura es simple y robusta:

1.  La app EdgeMind envía una solicitud segura (autenticada con una API Key) a este servidor.
2.  El servidor recibe la solicitud e inicia o reanuda una sesión con el CLI especificado (p. ej., `gemini chat`).
3.  El mensaje del usuario se pasa al CLI.
4.  La respuesta del CLI se captura y se envía de vuelta a la app EdgeMind, que la muestra al usuario.

## Instalación

Las instrucciones técnicas detalladas para instalar y configurar el servidor a través de Docker se pueden encontrar en el archivo [DEPLOYMENT.md](DEPLOYMENT.md).

---

*Descarga la app EdgeMind desde la Google Play Store:*
[https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind](https://play.google.com/store/apps/details?id=com.mmmbuto.edgemind)