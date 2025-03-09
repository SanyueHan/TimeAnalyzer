from enum import Enum


class TimeUnit(Enum):
    NS = 1.0
    US = 0.001
    MS = 0.000001
    S = 0.000000001

    def __init__(self, value: float):
        self._val = value

    def from_ns(self, num_of_ns: int) -> float:
        return num_of_ns * self._val
