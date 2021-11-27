from analyzer.metaclass import TimeAnalyzer
from test.python_built_in.examples.base import ComparatorBase


class Filter(ComparatorBase, metaclass=TimeAnalyzer):
    """
    In this class we compare the time consumption of filter the even numbers in a given range in different ways
    """
    def method_0(self):
        res = []
        for i in range(self.limit):
            if i % 2 == 0:
                res.append(i)

    def method_1(self):
        return [i for i in range(self.limit) if i % 2 == 0]

    def method_2(self):
        return list(filter(lambda i: i % 2 == 0, (i for i in range(self.limit))))

    def method_3(self):
        def fun(n):
            return n % 2 == 0

        return list(filter(fun, (i for i in range(self.limit))))
