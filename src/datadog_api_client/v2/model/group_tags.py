import warnings

warnings.warn("GroupTags is deprecated and doesn't do anything. It will be removed in a future version.")


class GroupTags:
    def __new__(cls, *args, **kwargs):
        return args[0]
