import time

class Timer:
    def __init__(self, block_name):
        self.block_name = block_name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"timer: block '{self.block_name}' executed in {elapsed_time:.3f} sec")

with Timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)
