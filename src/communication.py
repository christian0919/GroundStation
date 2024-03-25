import serial
import serial.tools.list_ports

class communication:

    def List_Serial_Ports():
        return serial.tools.list_ports.comports()

