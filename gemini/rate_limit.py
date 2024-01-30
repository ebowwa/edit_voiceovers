import threading
import time

class RateLimitedQueue:
    """
    A queue with rate limiting capabilities. Allows up to a maximum of 60 queries per minute.
    If the rate limit is exceeded, it pauses the API calls until it's safe to continue.
    """
    def __init__(self, max_rate=60, interval=60):
        import time
        import threading
        from collections import deque

        self.max_rate = max_rate
        self.interval = interval
        self.queue = deque()
        self.last_request_time = -interval
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self.process_queue)
        self.thread.daemon = True
        self.thread.start()

    def add_to_queue(self, func, *args, **kwargs):
        with self.lock:
            self.queue.append((func, args, kwargs))
        
    def process_queue(self):
        while True:
            with self.lock:
                if self.queue and self._can_process_next_request():
                    func, args, kwargs = self.queue.popleft()
                    threading.Thread(target=func, args=args, kwargs=kwargs).start()
            time.sleep(1)

    def _can_process_next_request(self):
        current_time = time.time()
        if current_time - self.last_request_time >= self.interval / self.max_rate:
            self.last_request_time = current_time
            return True
        return False