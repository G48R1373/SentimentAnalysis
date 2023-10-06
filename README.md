# SentimentAnalysis
#Approccio risolutivo:
#Sistemi su cui testare il codice:
#1. MacOs ARM64
#2. MacOs AMD64
#3. Windows 11 AMD64
#4. Windows 11 ARM64
#
#Installazione di Python su tutti i dispositivi
#Possibili strade:
#1. MacOs ARM64, MacOs AMD64, Windows 11 AMD64: Installazione immediata di Anaconda
#2. Windows 11 ARM64: (Miniforge, Miniconda, WLS2 -> Distribuzione Linux) ?
#
#Creazione diretta dell'environment python versione 3.8 su MacOs ARM64
#Attivazione dell'environment
#Installazione di librerie consigliate e di:
#1. vaderSentiment: Sentiment Analysis
#2. googletrans: traduzione dall'italiano all'inglese del messaggio (per poi utilizzare vaderSentiment, che di base prevede solo #l'inglese) letto dal file di testo message.txt
#
#Definizione dell'environment: pythonEnv.yml
#Creazione del main.py
#Se eseguito su Visual Studio Code: Esecuzione nell'apposito terminale usando come interprete pythonEnv
#Se eseguito da terminale: Assicurarsi di avere pythonEnv attivo
#Virtualizzazione della macchina virtuale Windows 11 con architettura ARM64 (Eseguita su MacOS ARM64)
#Virtualizzazione della macchina virtuale MacOs con architettura AMD64 (Eseguita su Windows 11 AMD64)
#Testare il codice sui 4 dispositivi
#(Al momento difficoltà con macchina virtuale Windows 11 architettura ARM64 -> Chiedere)
