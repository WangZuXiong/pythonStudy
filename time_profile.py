import time

def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)

        Logger.logger_error(">>>> Time {0}  {1}".format(fn.__name__, time.time() - start))

    return _wrapper