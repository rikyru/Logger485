# Logger485

Un'applicazione GUI in Python per acquisire, visualizzare e salvare dati da porta seriale RS485.

## Funzionalità

- Selezione porta seriale
- Lettura trama personalizzata con OPC 0xC5
- Estrazione temperatura e plotting in tempo reale
- Visualizzazione digitale di tempo e temperatura
- Esportazione dati in CSV
- Pulsanti Start / Stop

## Requisiti

- Python 3.8+
- PyQt5
- pyserial
- matplotlib

## Installa i pacchetti con:

```bash
pip install -r requirements.txt
```

##  Avvio:
```bash
python main.py
```

## Export dati:
Il tasto "Export" consente di salvare i dati letti in un file .csv con le colonne Time [s] e Temperature [°C].

## Freeze requirements:
```bash
pip freeze > requirements.txt
```




