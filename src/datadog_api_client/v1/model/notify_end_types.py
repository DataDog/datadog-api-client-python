import warnings

warnings.warn("NotifyEndTypes is deprecated and doesn't do anything. It will be removed in a future version.")


class NotifyEndTypes:
    def __new__(cls, *args, **kwargs):
        return args[0]
