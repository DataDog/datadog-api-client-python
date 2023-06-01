import warnings

warnings.warn("MonitorSearchCount is deprecated and doesn't do anything. It will be removed in a future version.")


class MonitorSearchCount:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
