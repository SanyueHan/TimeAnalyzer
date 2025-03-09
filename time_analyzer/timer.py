from collections import defaultdict
from time import time_ns

from .unit import TimeUnit


class Timer:
    stack = []
    timer = defaultdict(int)
    counter = defaultdict(int)

    def __init__(self, qualname):
        self._qualname = qualname
        self._start = None

    def __enter__(self):
        self.stack.append(self._qualname)
        self.counter[self._qualname] += 1
        self._start = time_ns()

    def __exit__(self, exc_type, exc_value, traceback):
        delta = time_ns() - self._start
        self.stack.pop()

        self.timer[self._qualname] += delta
        if self.stack:
            caller_name = self.stack[-1]
            self.timer[caller_name] -= delta

    @classmethod
    def explain_performance_by_name(cls, unit: TimeUnit = TimeUnit.S, precision: int = 2):
        total = sum(cls.timer.values())
        print(f"Overall Time: {unit.from_ns(total):.{precision}f}{unit.name.lower()}")
        data = [("name", f"sum({unit.name.lower()})", "count", "proportion")]
        for name in sorted(cls.timer.keys(), key=cls.timer.get, reverse=True):
            data.append((name, f"{unit.from_ns(cls.timer[name]):.{precision}f}", f"{cls.counter[name]}", f"{cls.timer[name] * 100 / total:.2f}%"))
        cls.__display_table(data, ('<', '>', '>', '>'))

    @staticmethod
    def __display_table(data, fmt, sep='    '):
        n = len(fmt)
        assert all(len(row) == n for row in data)
        max_len = [0] * n
        for i in range(n):
            max_len[i] = max(len(row[i]) for row in data)
        for row in data:
            print(sep.join(f"{row[i]:{fmt[i]}{max_len[i]}}" for i in range(n)))
