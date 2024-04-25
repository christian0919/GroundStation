import serial
import serial.tools.list_ports
import time
from config import config

class communication:
    def __init__(self):
        self.serial_port =""
        self.configuration = config()
        self.Set_Parameters_Values(self)

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

    def Set_Parameters_Values(self , PI = 0 , PE = 0 , ALT = 0 , TI = 0 , TE = 0 , LAT = 0
                              , LONG = 0 , GX = 0 , GY = 0 , GZ = 0 , ACX = 0, ACY = 0 , ACZ = 0, BATT = 0):
        
        self.presion_Interna = PI
        self.presion_Externa = PE
        
        self.altitud = ALT

        self.Temperature_Intern = TI
        self.Temperature_Extern = TE

        self.latitud = LAT
        self.longitud = LONG

        self.giro_x = GX
        self.giro_y = GY
        self.giro_z = GZ

        self .aceleration_x = ACX
        self.aceleration_y = ACY
        self.aceleration_z = ACZ
        self.battery = BATT

    def Split_Data (self, data):
        print(data)
        splited = data.split(":")
        
        self.presion_Interna = int(splited[0])
        self.presion_Externa = int(splited[1])
        
        self.altitud = int(splited[2])

        self.Temperature_Intern = int(splited[3])
        self.Temperature_Extern = int(splited[4])

        self.latitud = int(splited[5])
        self.longitud = int(splited[6])

        self.giro_x = int(splited[7])
        self.giro_y = int(splited[8])
        self.giro_z = int(splited[9])

        self.aceleration_x = int(splited[10])
        self.aceleration_y = int(splited[11])
        self.aceleration_z = int(splited[12])
        self.battery = int(splited[13])
#Get Data functions
    def get_Presion_I(self):
       return self.presion_Interna
    def get_Presion_E(self):
       return self.presion_Externa
    def get_altitud (self):
        return self.altitud
    def get_Temperature_I (self):
        return self.Temperature_Intern
    def get_Temperature_E (self):
        return self.Temperature_Extern
    def get_latitud (self):
        return self.latitud
    def get_longitud (self):
        return self.longitud
    def get_giro_x (self):
        return self.giro_x
    def get_giro_y (self):
        return self.giro_y
    def get_giro_z (self):
        return self.giro_z
    def get_aceleracion_x (self):
        return self.aceleration_x
    def get_aceleracion_y (self):
        return self.aceleration_y
    def get_aceleracion_z (self):
        return self.aceleration_z
    def get_battery (self):
        return self.battery