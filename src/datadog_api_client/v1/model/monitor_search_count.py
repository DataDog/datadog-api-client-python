import warnings

warnings.warn("MonitorSearchCount is deprecated and doesn't do anything. It will be removed in a future version.")


class MonitorSearchCount:
    def __new__(cls, *args, **kwargs):
        return args[0]
