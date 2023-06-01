import warnings

warnings.warn("GCPAccountListResponse is deprecated and doesn't do anything. It will be removed in a future version.")


class GCPAccountListResponse:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
