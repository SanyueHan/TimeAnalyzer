from analyzer.metaclass import TimeAnalyzer
from test.python_built_in.examples.base import ComparatorBase


class Sum(ComparatorBase, metaclass=TimeAnalyzer):
    """
    In this class we compare the time consumption of summing the numbers in a given range in different ways
    """
    def method_0(self):
        s = 0
        i = 0
        while i != self.limit:
            s += i
            i += 1
        return s

    def method_1(self):
        s = 0
        for i in range(self.limit):
            s += i
        return s

    def method_2(self):
        return sum(i for i in range(self.limit))
