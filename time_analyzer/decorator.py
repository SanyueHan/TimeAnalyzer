import functools

from .config import DIAGNOSE_TIME
from .timer import Timer


def cumulate_time(fun):
    if DIAGNOSE_TIME:
        @functools.wraps(fun)
        def fun_timed(*args, **kw):
            with Timer(fun.__qualname__):
                return fun(*args, **kw)

        return fun_timed
    else:
        return fun
