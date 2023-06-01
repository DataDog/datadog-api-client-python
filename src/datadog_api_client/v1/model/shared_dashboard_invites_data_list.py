import warnings

warnings.warn(
    "SharedDashboardInvitesDataList is deprecated and doesn't do anything. It will be removed in a future version."
)


class SharedDashboardInvitesDataList:
    def __new__(cls, *args, **kwargs):
        return args[0]
