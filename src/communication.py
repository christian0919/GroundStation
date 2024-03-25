import serial
import serial.tools.list_ports
import time

class communication:
    def __init__(self):
        self.serial_Port = ""
        self.puerto_serial = serial.Serial('COM5', 115200, timeout=1)

    def List_Serial_Ports():
        return serial.tools.list_ports.comports()

    def Send_AT_Command(self,command):
        self.puerto_serial.write((command + '\r\n').encode())  # Agrega el retorno de carro y la nueva línea requeridos por los comandos AT
        time.sleep(0.1)  #Espera breve para que el módulo responda
        respuesta = self.puerto_serial.readlines()
        return respuesta
