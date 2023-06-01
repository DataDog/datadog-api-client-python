import warnings

warnings.warn("MetricCustomAggregations is deprecated and doesn't do anything. It will be removed in a future version.")


class MetricCustomAggregations:
    def __new__(cls, *args, **kwargs):
        return args[0]
