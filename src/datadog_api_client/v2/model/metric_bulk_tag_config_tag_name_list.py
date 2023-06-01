import warnings

warnings.warn(
    "MetricBulkTagConfigTagNameList is deprecated and doesn't do anything. It will be removed in a future version."
)


class MetricBulkTagConfigTagNameList:
    def __new__(cls, *args, **kwargs):
        return args[0]
