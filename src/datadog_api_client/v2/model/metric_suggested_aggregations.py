import warnings

warnings.warn(
    "MetricSuggestedAggregations is deprecated and doesn't do anything. It will be removed in a future version."
)


class MetricSuggestedAggregations:
    def __new__(cls, *args, **kwargs):
        return args[0]
