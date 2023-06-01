import warnings

warnings.warn(
    "LogsAggregateBucketValueTimeseries is deprecated and doesn't do anything. It will be removed in a future version."
)


class LogsAggregateBucketValueTimeseries:
    def __new__(cls, *args, **kwargs):
        return args[0]
