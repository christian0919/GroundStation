import json

class config:
    def __init__(self):
        self.__LoRa_ADDRESS = 0
        self.__LoRa_NETWORKID = 0
        self.__LoRa_BAND = 0
        self.__LoRa_SPREADING_FACTOR = 0
        self.__LoRa_BANDWIDTH = 0
        self.__LoRa_CODING_RATE = 0
        self.__LoRa_PROGRAMMED_PREAMBLE = 0
        self.__path = "config.json"

        self.UpdateValues()

    def UpdateValues(self):

        try:
            with open(self.__path, 'r') as archivo:
                data = json.load(archivo)
        except FileNotFoundError:
            print(f"El archivo {self.__path} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {self.__path}.")

        self.__LoRa_ADDRESS = data["LoRa_ADDRESS"]
        self.__LoRa_NETWORKID = data["LoRa_NETWORKID"]
        self.__LoRa_BAND = data["LoRa_BAND"]
        self.__LoRa_SPREADING_FACTOR = data["LoRa_SPREADING_FACTOR"]
        self.__LoRa_BANDWIDTH = data["LoRa_BANDWIDTH"]
        self.__LoRa_CODING_RATE = data["LoRa_CODING_RATE"]
        self.__LoRa_PROGRAMMED_PREAMBLE = data["LoRa_PROGRAMMED_PREAMBLE"]

    def Set_Values(self,ADDRESS,NETWORKID,BAND,SPREAD,BANDWIDTH,CODING,PREAMBLE):

        try:
            #Read from file
            with open(self.__path, 'r') as archivo:
                data = json.load(archivo)
            #Assigment of new values
            data["LoRa_ADDRESS"]  = ADDRESS
            data["LoRa_NETWORKID"] = NETWORKID
            data["LoRa_BAND"] = BAND
            data["LoRa_SPREADING_FACTOR"] = SPREAD
            data["LoRa_BANDWIDTH"] = BANDWIDTH
            data["LoRa_CODING_RATE"] = CODING
            data["LoRa_PROGRAMMED_PREAMBLE"] = PREAMBLE
            #Write in file
            with open(self.__path, 'w') as archivo:
                json.dump(data, archivo, indent=4)
            self.UpdateValues()
        except FileNotFoundError:
            print(f"El archivo {self.__path} no se encontró.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {self.__path}.")

    def get_LoRa_ADDRESS(self):
        return self.__LoRa_ADDRESS
    def get_LoRa_NETWORKID(self):
        return self.__LoRa_NETWORKID
    def get_LoRa_BAND(self):
        return self.__LoRa_BAND
    def get_LoRa_SPREADING_FACTOR(self):
        return self.__LoRa_SPREADING_FACTOR
    def get_LoRa_BANDWIDTH(self):
        return self.__LoRa_BANDWIDTH
    def get_LoRa_CODING_RATE(self):
        return self.__LoRa_CODING_RATE
    def get_LoRa_PROGRAMMED_PREAMBLE(self):
        return self.__LoRa_PROGRAMMED_PREAMBLE
    