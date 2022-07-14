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

    @classmethod
    def explain_performance_by_name(cls):
        print(f"Total Time: {sum(cls.recorder.values())}")
        for t, n in sorted([(t, n) for n, t in cls.recorder.items()], reverse=True):
            print(f"{t:10.2f}ms    {n}")

    @classmethod
    def explain_performance_by_class(cls):
        print("Divided by Class: ")
        classes = {}
        for n, t in cls.recorder.items():
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
            print(f"{cls_}    {classes[cls_].pop('total')}ms")
            for t, n in sorted([(t, n) for n, t in classes[cls_].items()], reverse=True):
                print(f"    {t:10.2f}ms    {n}")
