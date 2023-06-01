import warnings

warnings.warn(
    "TimeseriesFormulaRequestQueries is deprecated and doesn't do anything. It will be removed in a future version."
)


class TimeseriesFormulaRequestQueries:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
