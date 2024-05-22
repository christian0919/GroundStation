from datetime import datetime

class TimeManager:
    def __init__(self):
        self.time = ""

    def get_Time(self):
        self.time = datetime.now().strftime("%H:%M:%S")
        return self.time