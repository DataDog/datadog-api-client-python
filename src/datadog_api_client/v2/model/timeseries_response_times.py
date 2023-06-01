import warnings

warnings.warn("TimeseriesResponseTimes is deprecated and doesn't do anything. It will be removed in a future version.")


class TimeseriesResponseTimes:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
