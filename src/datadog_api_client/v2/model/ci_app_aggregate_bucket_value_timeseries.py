import warnings

warnings.warn(
    "CiAppAggregateBucketValueTimeseries is deprecated and doesn't do anything. It will be removed in a future version."
)


class CiAppAggregateBucketValueTimeseries:
    def __new__(cls, *args, **kwargs):
        return args[0]
