import asyncio

class Alarm:
    def __init__(self, lights):
        self.lights = lights
        self.alarm_time = None
        asyncio.ensure_future(self.alarm_clock_function())
    
    # alarm
    @asyncio.coroutine
    def alarm_clock_function(self):
        while True:
            self.alarm_time = self.alarm_time + 1
            if self.alarm_time == 1000:
                print('hello', self.alarm_time)
                self.alarm_time = 0


    