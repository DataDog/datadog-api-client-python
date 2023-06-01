import warnings

warnings.warn(
    "SecurityMonitoringSignalIncidentIds is deprecated and doesn't do anything. It will be removed in a future version."
)


class SecurityMonitoringSignalIncidentIds:
    def __new__(cls, *args, **kwargs):
        return args[0]
