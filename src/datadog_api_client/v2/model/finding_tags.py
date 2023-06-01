import warnings

warnings.warn("FindingTags is deprecated and doesn't do anything. It will be removed in a future version.")


class FindingTags:
    def __new__(cls, *args, **kwargs):
        return args[0]
