import serial
import serial.tools.list_ports
import time
from config import config

class communication:
    def __init__(self):
        self.serial_port =""
        self.configuration = config()

    def Send_AT_Command(self,command):
        self.serial_port.write((command + '\r\n').encode())  # Agrega el retorno de carro y la nueva línea requeridos por los comandos AT
        time.sleep(0.1)  #Espera breve para que el módulo responda
        respuesta = self.serial_port.readlines()
        print(respuesta)
    
    def Get_Cansat_Data(self):
        data = self.serial_port.readline().decode().strip()
        if(data != "" or data !=''):
            #print("Datos recibidos:", data)
            filtered = data.split("|")
            return str(filtered[1])
        return ""

    def Set_Serial_Port(self,port):
        self.serial_port = serial.Serial(port, 115200, timeout=1)

    def InitializeLora(self):
        self.configuration.UpdateValues()
        self.Send_AT_Command("AT")
        self.Send_AT_Command("AT+RESET")
        self.Send_AT_Command("AT+BAND=" + str(self.configuration.get_LoRa_BAND()))
        self.Send_AT_Command("AT+NETWORKID=" + str(self.configuration.get_LoRa_NETWORKID()))
        self.Send_AT_Command("AT+ADDRESS=" + str(self.configuration.get_LoRa_ADDRESS()))
        self.Send_AT_Command("AT+PARAMETER=" + 
                            str(self.configuration.get_LoRa_SPREADING_FACTOR()) + "," +
                            str(self.configuration.get_LoRa_BANDWIDTH()) + "," +
                            str(self.configuration.get_LoRa_CODING_RATE()) + "," +
                            str(self.configuration.get_LoRa_PROGRAMMED_PREAMBLE()))
        print("LoRa initialized")
        
