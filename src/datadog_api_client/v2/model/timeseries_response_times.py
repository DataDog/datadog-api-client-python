import warnings

warnings.warn("TimeseriesResponseTimes is deprecated and doesn't do anything. It will be removed in a future version.")


class TimeseriesResponseTimes:
    def __new__(cls, *args, **kwargs):
        return args[0]
