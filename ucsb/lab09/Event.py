class Event:
    def __init__(self, day, time, location):
        self.day = day
        self.time = time
        self.location = location.upper()

    def __eq__(self, other):
        return True if self.day == other.day and self.time == other.time  and self.location == other.location else False

    def __str__(self):
        return f"{self.day} {self.format(self.time)}, {self.location}"

    @staticmethod
    def format(time):
        return f"{time[0] // 100:0>2}:{time[0] % 100:0>2} - {time[1] // 100:0>2}:{time[1] % 100:0>2}"

