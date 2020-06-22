import functools


def api_call(f):
    @functools.wraps(f)
    def wrapper(self, *args, **kwargs):
        ret = f(self, *args, **kwargs)
        print('{} returns {}'. format(f.__name__, ret))
        return ret


def api_setter(f):
    @functools.wraps(f)
    def wrapper(self, *args, **kwargs):
        pass