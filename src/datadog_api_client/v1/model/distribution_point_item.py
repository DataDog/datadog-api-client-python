import warnings

warnings.warn("DistributionPointItem is deprecated and doesn't do anything. It will be removed in a future version.")


class DistributionPointItem:
    def __new__(cls, *args, **kwargs):
        return args[0]
