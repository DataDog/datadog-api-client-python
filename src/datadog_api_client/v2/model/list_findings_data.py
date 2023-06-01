import warnings

warnings.warn("ListFindingsData is deprecated and doesn't do anything. It will be removed in a future version.")


class ListFindingsData:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
