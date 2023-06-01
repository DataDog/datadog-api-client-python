import warnings

warnings.warn(
    "MetricBulkTagConfigEmailList is deprecated and doesn't do anything. It will be removed in a future version."
)


class MetricBulkTagConfigEmailList:
    def __new__(cls, *args, **kwargs):
        return args[0]
