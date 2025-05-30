from PyQt5.QtCore import QObject, pyqtSignal
import time
import random
import serial


class SerialWorker(QObject):
    data_received = pyqtSignal(float)

    def __init__(self, port, baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.running = True

    def run(self):
        try:
            with serial.Serial(self.port, self.baudrate, timeout=1) as ser:
                buffer = bytearray()

                while self.running:
                    if ser.in_waiting:
                        byte = ser.read(1)
                        buffer += byte

                        # cerca inizio e fine trama
                        if buffer and buffer[0] != 0x80:
                            buffer.pop(0)

                        if len(buffer) >= 8 and buffer[0] == 0x80 and buffer[7] == 0x81:
                            self.handle_frame(buffer[:8])
                            buffer.clear()

                    time.sleep(0.01)

        except Exception as e:
            print(f"[ERRORE SERIALE] {e}")

    def handle_frame(self, frame):
        if frame[0] == 0x80 and frame[-1] == 0x81 and frame[2] == 0xC5:
            raw_temp = frame[5]
            temp_c = raw_temp #- 0x21  # -29°C = 0x08
            self.data_received.emit(temp_c)


#Versione simulata per testare il codice senza hardware reale
""" class SerialWorker(QObject):
    data_received = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            # Simula una trama valida
            frame = [0x80, 0x08, 0xC5, 0xB0, 0x40, random.randint(0x08, 0x40), 0xAA, 0x81]
            self.handle_frame(frame)
            time.sleep(1)

    def handle_frame(self, frame):
        if len(frame) >= 8 and frame[0] == 0x80 and frame[-1] == 0x81:
            if frame[2] == 0xC5:
                raw_temp = frame[5]
                temp_c = raw_temp - 0x21  # 0x08 → -29°C
                print(f"[DEBUG] Ricevuta temperatura: {temp_c}°C")
                self.data_received.emit(temp_c)
 """