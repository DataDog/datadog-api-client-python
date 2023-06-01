import warnings

warnings.warn(
    "TimeseriesResponseSeriesList is deprecated and doesn't do anything. It will be removed in a future version."
)


class TimeseriesResponseSeriesList:
    def __new__(cls, *args, **kwargs):
        return args[0]
