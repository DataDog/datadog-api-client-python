import warnings

warnings.warn("DistributionPointData is deprecated and doesn't do anything. It will be removed in a future version.")


class DistributionPointData:
    def __new__(cls, *args, **kwargs):
        return args[0]
