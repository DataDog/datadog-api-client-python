import warnings

warnings.warn("EventsQueryGroupBys is deprecated and doesn't do anything. It will be removed in a future version.")


class EventsQueryGroupBys:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
