@echo off
echo Generazione file ui_mainwindow.py da ui_mainwindow.ui...
pyuic5 ui_mainwindow.ui -o ui_mainwindow.py
if %errorlevel%==0 (
    echo Fatto! File aggiornato correttamente.
) else (
    echo Errore nella generazione del file UI.
)
pause
