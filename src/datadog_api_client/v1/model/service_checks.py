import warnings

warnings.warn("ServiceChecks is deprecated and doesn't do anything. It will be removed in a future version.")


class ServiceChecks:
    def __new__(cls, *args, **kwargs):
        return args[0]
