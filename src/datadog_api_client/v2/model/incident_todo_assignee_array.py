import warnings

warnings.warn(
    "IncidentTodoAssigneeArray is deprecated and doesn't do anything. It will be removed in a future version."
)


class IncidentTodoAssigneeArray:
    def __new__(cls, *args, **kwargs):
        return args[0]
