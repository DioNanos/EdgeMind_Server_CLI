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