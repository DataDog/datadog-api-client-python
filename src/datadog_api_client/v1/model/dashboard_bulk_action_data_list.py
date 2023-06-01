import warnings

warnings.warn(
    "DashboardBulkActionDataList is deprecated and doesn't do anything. It will be removed in a future version."
)


class DashboardBulkActionDataList:
    def __new__(cls, *args, **kwargs):
        return args[0]
