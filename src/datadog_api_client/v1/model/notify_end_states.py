import warnings

warnings.warn("NotifyEndStates is deprecated and doesn't do anything. It will be removed in a future version.")


class NotifyEndStates:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
