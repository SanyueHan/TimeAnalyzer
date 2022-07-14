from collections import defaultdict
from time import time


class Timer:
    stack = []
    recorder = defaultdict(lambda: 0.0)

    def __init__(self, qualname):
        self._qualname = qualname
        self._start = None

    def __enter__(self):
        self.stack.append(self._qualname)
        self._start = time()

    def __exit__(self, exc_type, exc_value, traceback):
        delta = time() - self._start
        self.stack.pop()

        self.recorder[self._qualname] += delta
        if self.stack:
            caller_name = self.stack[-1]
            self.recorder[caller_name] -= delta
