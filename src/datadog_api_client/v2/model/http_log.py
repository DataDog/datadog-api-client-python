import warnings

warnings.warn("HttpLog is deprecated and doesn't do anything. It will be removed in a future version.")


class HttpLog:
    def __new__(cls, *args, **kwargs):
        return args[0]
