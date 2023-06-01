import warnings

warnings.warn(
    "RumAggregateBucketValueTimeseries is deprecated and doesn't do anything. It will be removed in a future version."
)


class RumAggregateBucketValueTimeseries:
    def __new__(cls, *args, **kwargs):
        return args[0]
