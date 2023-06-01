import warnings

warnings.warn(
    "UsageAttributionAggregates is deprecated and doesn't do anything. It will be removed in a future version."
)


class UsageAttributionAggregates:
    def __new__(cls, *args, **kwargs):
        return args[0]
