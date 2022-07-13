import time

from .config import DIAGNOSE_TIME
from .globals import GLOBAL_STACK, TIME_RECORDER


def cumulate_time(fun):
    if DIAGNOSE_TIME:
        def fun_with_time(*args, **kw):
            key = fun.__qualname__
            GLOBAL_STACK.append(key)
            ts = time.time()
            result = fun(*args, **kw)
            te = time.time()
            GLOBAL_STACK.pop()
            delta = (te - ts) * 1000
            TIME_RECORDER[key] += delta

            # remove this time from the parent function
            if GLOBAL_STACK:
                key = GLOBAL_STACK[-1]
                TIME_RECORDER[key] -= delta
            return result

        return fun_with_time
    else:
        return fun
