import warnings

warnings.warn(
    "SensitiveDataScannerStandardPatternsResponse is deprecated and doesn't do anything. It will be removed in a future version."
)


class SensitiveDataScannerStandardPatternsResponse:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        return args[0]
