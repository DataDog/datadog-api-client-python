import warnings

warnings.warn("AzureAccountListResponse is deprecated and doesn't do anything. It will be removed in a future version.")


class AzureAccountListResponse:
    def __new__(cls, *args, **kwargs):
        return args[0]
