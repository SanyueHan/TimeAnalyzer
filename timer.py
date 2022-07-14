from collections import defaultdict
from time import time


class Timer:
    stack = []
    time_recorder = defaultdict(float)
    count_recorder = defaultdict(int)

    def __init__(self, qualname):
        self._qualname = qualname
        self._start = None

    def __enter__(self):
        self.stack.append(self._qualname)
        self.count_recorder[self._qualname] += 1
        self._start = time()

    def __exit__(self, exc_type, exc_value, traceback):
        delta = time() - self._start
        self.stack.pop()

        self.time_recorder[self._qualname] += delta
        if self.stack:
            caller_name = self.stack[-1]
            self.time_recorder[caller_name] -= delta

    @classmethod
    def explain_performance_by_name(cls):
        print(f"Overall Time: {sum(cls.time_recorder.values())}s")
        data = [("name", "total time(s)", "count")]
        for n in sorted(cls.time_recorder.keys(), key=cls.time_recorder.get, reverse=True):
            data.append((n, f"{cls.time_recorder[n]:.2f}", f"{cls.count_recorder[n]}"))
        cls.__display_table(data, ('<', '>', '>'))

    @classmethod
    def explain_performance_by_class(cls):
        print("Divided by Class: ")
        classes = {}
        for n, t in cls.time_recorder.items():
            if '.' in n:
                class_name, method_name = n.split('.')
                if class_name in classes:
                    classes[class_name][method_name] = t
                else:
                    classes[class_name] = {method_name: t}
            # todo: normal functions
        for cls_method_dict in classes.values():
            cls_method_dict['total'] = sum(cls_method_dict.values())
        for cls_ in sorted(classes.keys(), key=lambda i: classes[i]['total'], reverse=True):
            print(f"{cls_}    {classes[cls_].pop('total')}s")
            for t, n in sorted([(t, n) for n, t in classes[cls_].items()], reverse=True):
                print(f"    {t:10.2f}s    {n}")

    @staticmethod
    def __display_table(data, fmt, sep='    '):
        n = len(fmt)
        assert all(len(row) == n for row in data)
        max_len = [0] * n
        for i in range(n):
            max_len[i] = max(len(row[i]) for row in data)
        for row in data:
            print(sep.join(f"{row[i]:{fmt[i]}{max_len[i]}}" for i in range(n)))
