import warnings

warnings.warn("GcpAccountListResponse is deprecated and doesn't do anything. It will be removed in a future version.")


class GcpAccountListResponse:
    def __new__(cls, *args, **kwargs):
        return args[0]
