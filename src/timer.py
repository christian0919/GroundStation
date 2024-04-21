class TimeManager:
    def __init__(self):
        self.initialize_Time()

    def initialize_Time(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        

    def update_time(self):
        self.milliseconds += 100
        if self.milliseconds >= 1000:
            self.seconds += 1
            self.milliseconds = 0
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes >= 60:
            self.hours += 1
            self.minutes = 0

    def get_time(self):
        return self.hours, self.minutes, self.seconds, self.milliseconds