class Event:
    def __init__(self, day, time, location):
        self.day = day
        self.time = time
        self.location = location.upper()

    def __eq__(self, rhs):
        return self.day == rhs.day and self.time == rhs.time and self.location == rhs.location

    def __str__(self):
        return f"{self.day} {self.format_time()}, {self.location}"

    def format_time(self):
        return f"{self.time[0]//100:0>2}:{self.time[0]%100:0>2} - {self.time[1]//100:0>2}:{self.time[1]%100:0>2}"


def format(time):
    return f"{time[0]//100:0>2}:{time[0]%100:0>2} - {time[1]//100:0>2}:{time[1]%100:0>2}"
