import time

from analyzer.globals import GLOBAL_STACK, TIME_RECORDER


def cumulate_time(fun):
    def fun_with_time(*args, **kw):
        key = fun.__qualname__
        # todo: static methods
        GLOBAL_STACK.append(key)
        ts = time.time()
        result = fun(*args, **kw)
        te = time.time()
        GLOBAL_STACK.pop()
        delta = (te - ts) * 1000
        if key in TIME_RECORDER:
            TIME_RECORDER[key] += delta
        else:
            TIME_RECORDER[key] = delta

        if GLOBAL_STACK:
            key = GLOBAL_STACK[-1]
            if key in TIME_RECORDER:
                TIME_RECORDER[key] -= delta
            else:
                TIME_RECORDER[key] = -delta
        return result
    return fun_with_time
