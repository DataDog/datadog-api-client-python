import warnings

warnings.warn("TimeseriesResponseValues is deprecated and doesn't do anything. It will be removed in a future version.")


class TimeseriesResponseValues:
    def __new__(cls, *args, **kwargs):
        return args[0]
