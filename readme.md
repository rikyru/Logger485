# Logger485

Un'applicazione GUI in Python per acquisire, visualizzare e salvare dati da porta seriale RS485.

## Funzionalità

- Selezione porta seriale
- Lettura trama personalizzata con OPC 0xC5
- Estrazione temperatura e plotting in tempo reale
- Visualizzazione digitale di tempo e temperatura
- Esportazione dati in CSV
- Pulsanti Start / Stop

## Export dati:
Il tasto "Export" consente di salvare i dati letti in un file .csv con le colonne Time [s] e Temperature [°C].

## Guida Sviluppo e Mantenimeto

### Requisiti

- Estensione python per VsCode
- Estensione Qt for Python per VsCode
- Python 3.8+
- PyQt5
- pyserial
- matplotlib


### Ambiente virtuale
Per lavorare sul progetto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Questo crea un ambiente virtuale e installa i pacchetti nell'ambiente virtuale

### Modificare l'interfaccia grafica
1) Aprire Qt Designer:
```bash
pyqt5-tools designer
```
2) Salvare ui_mainwindow.ui nella root

3) Esegui il file batch incluso per aggiornare ui_mainwindow.py
```bash
generate_ui.bat
```
    Non modificare ui_mainwindow.py a mano, viene sovrascritto ogni volta!

### Suggerimenti
- Le modifiche alla logica dell'app vanno in main.py e serial_worker.py
- Le modifiche alla GUI vanno fatte in ui_mainwindow.ui, poi ricompilate

#### Freeze requirements:
Per aggiungere nuove dipendenze
```bash
pip freeze > requirements.txt
```

## Creazione dell'eseguibile .exe
Per generare un file eseguibile da distribuire senza Python:
### 1. Installa `pyinstaller`

Assicurati di aver attivato il venv:

```bash
pip install pyinstaller
```
### 2. Genera il .exe
```bash
pyinstaller --onefile --windowed main.py
```
--onefile -> tutto in un unico exe
--windowed	-> non apre il terminale quando lanci l’app (solo GUI)
### 3. Dove si trova
Nella cartella 
dist/main.exe
Puoi rinominarlo e copiarlo dove vuoi.

### NOTE IMPORTANTI
- Se l’eseguibile non parte su un altro PC, assicurati che abbia:

1) le librerie di runtime C++ di Visual Studio (VC_redist)

2) tutti i file esterni necessari (es. .ui compilato, file di supporto)

3) Se usi file esterni, includili usando --add-data (vedi documentazione PyInstaller)





##  Avvio:
```bash
python main.py
```





