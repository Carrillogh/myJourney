# Timer for starting and stopping a timer
import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        print("Timer started.")

    def stop(self):
        """Stop the timer and return the elapsed time."""
        if self.start_time is None:
            print("Timer has not been started.")
            return None
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds.")
        return elapsed_time
    # Balance