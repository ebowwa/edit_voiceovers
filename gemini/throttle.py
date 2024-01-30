import time

class Throttle:
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit
        self.timestamps = []

    def wait(self):
        current_time = time.time()
        while self.timestamps and current_time - self.timestamps[0] > 60:
            self.timestamps.pop(0)

        if len(self.timestamps) >= self.rate_limit:
            time_to_wait = 60 - (current_time - self.timestamps[0])
            time.sleep(time_to_wait)
            self.timestamps.pop(0)

        self.timestamps.append(time.time())