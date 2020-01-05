import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.10f} ms'.format(f.__qualname__, (time2-time1)*1000.0))

        return ret
    return wrap
