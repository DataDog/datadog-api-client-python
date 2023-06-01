import warnings

warnings.warn("DistributionPoint is deprecated and doesn't do anything. It will be removed in a future version.")


class DistributionPoint:
    def __new__(cls, *args, **kwargs):
        return args[0]
