import warnings

warnings.warn(
    "SecurityMonitoringSignalIncidentIds is deprecated and doesn't do anything. It will be removed in a future version."
)


class SecurityMonitoringSignalIncidentIds:
    """Deprecated, please don't use."""

    def __new__(cls, *args, **kwargs):
        if not args:
            raise TypeError("Only support a single argument")
        return args[0]
