import warnings

warnings.warn(
    "SensitiveDataScannerGetConfigIncludedArray is deprecated and doesn't do anything. It will be removed in a future version."
)


class SensitiveDataScannerGetConfigIncludedArray:
    def __new__(cls, *args, **kwargs):
        return args[0]
