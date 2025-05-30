from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import serial.tools.list_ports  # <-- per trovare le COM
from PyQt5.QtCore import QThread
from serial_worker import SerialWorker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import time 
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.start_time = None
        self.time_timer = QTimer()
        self.time_timer.setInterval(100)  # ogni 100ms
        self.time_timer.timeout.connect(self.update_time_display)

        # Riempie la comboBox con le COM disponibili
        self.populate_serial_ports()

        # registra la callback per il pulsante Start e Stop e Export
        self.ui.pushButton_Start.clicked.connect(self.on_start_clicked)
        self.ui.pushButton_Stop.clicked.connect(self.on_stop_clicked)
        self.ui.pushButton_Export.clicked.connect(self.on_export_clicked)

        # Inizializza matplotlib
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.widget_plot.layout().addWidget(self.canvas)

        # Accesso all'asse
        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.set_title("Temperatura in tempo reale")
        self.ax.set_xlabel("Campione")
        self.ax.set_ylabel("°C")

        # Buffer dei dati
        self.times = []
        self.temps = []

    def populate_serial_ports(self):
        # Ottieni tutte le COM disponibili
        ports = serial.tools.list_ports.comports()
        port_names = [port.device for port in ports]  # es: ['COM3', 'COM4']

        # Svuota e riempie la comboBox
        self.ui.comboBox_port.clear()
        self.ui.comboBox_port.addItems(port_names)

    def update_time_display(self):
        if self.start_time is not None:
            tempo_trascorso = time.time() - self.start_time
            self.ui.lcdNumber_time.display(round(tempo_trascorso, 1))

    def update_plot(self, temp_c):
        tempo_trascorso = time.time() - self.start_time  
        self.ui.lcdNumber_temperature.display(round(temp_c, 1))  
        self.times.append(tempo_trascorso)
        self.temps.append(temp_c)
        if len(self.temps) > 100:
            self.temps.pop(0)
            self.times.pop(0)

        self.ax.clear()
        self.ax.plot(self.temps)
        self.ax.set_title("Temperature")
        self.ax.set_xlabel("Time [s]")
        self.ax.set_ylabel("°C")
        self.ax.legend()
        self.canvas.figure.tight_layout()
        self.canvas.draw()

    def on_start_clicked(self):
        selected_port = self.ui.comboBox_port.currentText()
        if selected_port:
            print(f"Porta selezionata: {selected_port}")
            self.thread = QThread()
            self.worker = SerialWorker(selected_port, baudrate=9600)
            self.worker.moveToThread(self.thread)
            self.worker.data_received.connect(self.update_plot)  # da implementare dopo
            self.thread.started.connect(self.worker.run)
            self.thread.start()
            self.start_time = time.time()
            self.temps.clear()  # Pulisce i dati precedenti
            self.times.clear()  # Pulisce i tempi precedenti
            self.time_timer.start()
        else:
            print("Nessuna porta selezionata.")

    def on_stop_clicked(self):
        # Ferma il thread della seriale
        if self.worker:
            self.worker.running = False
            self.thread.quit()
            self.thread.wait()
            self.worker = None
            self.thread = None

        # Ferma anche il timer del tempo
        self.time_timer.stop()

        print("Misurazione fermata.")

    def on_export_clicked(self):
        if not self.times or not self.temps:
            print("Nessun dato da esportare.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Salva dati", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Time", "Temperature"])
                for t, temp in zip(self.times, self.temps):
                    writer.writerow([round(t, 2), round(temp, 2)])
            print(f"Dati esportati in {file_path}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
