import warnings

warnings.warn("ListFindingsData is deprecated and doesn't do anything. It will be removed in a future version.")


class ListFindingsData:
    def __new__(cls, *args, **kwargs):
        return args[0]
