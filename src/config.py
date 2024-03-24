import json

class config:
    def __init__(self):
        self.LoRa_ADDRESS = 0
        self.LoRa_NETWORKID = 0
        self.LoRa_BAND = 0
        self.LoRa_SPREADING_FACTOR = 0
        self.LoRa_BANDWIDTH = 0
        self.LoRa_CODING_RATE = 0
        self.LoRa_PROGRAMMED_PREAMBLE = 0
        

    def UpdateValues(self):


        self.LoRa_ADDRESS = 0
        self.LoRa_NETWORKID = 0
        self.LoRa_BAND = 0
        self.LoRa_SPREADING_FACTOR = 0
        self.LoRa_BANDWIDTH = 0
        self.LoRa_CODING_RATE = 0
        self.LoRa_PROGRAMMED_PREAMBLE = 0

    def getLoRa_ADDRESS(self):
        return self.LoRa_ADDRESS
    def getLoRa_NETWORKID(self):
        return self.LoRa_NETWORKID
    def getLoRa_BAND(self):
        return self.LoRa_BAND
    def getLoRa_SPREADING_FACTOR(self):
        return self.LoRa_SPREADING_FACTOR
    def getLoRa_BANDWIDTH(self):
        return self.LoRa_BANDWIDTH
    def getLoRa_CODING_RATE(self):
        return self.LoRa_CODING_RATE
    def getLoRa_PROGRAMMED_PREAMBLE(self):
        return self.LoRa_PROGRAMMED_PREAMBLE
    