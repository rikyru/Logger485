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




## Installa i pacchetti con:

```bash
pip install -r requirements.txt
```

##  Avvio:
```bash
python main.py
```
## Freeze requirements:
```bash
pip freeze > requirements.txt
```




