import warnings

warnings.warn(
    "ScalarFormulaRequestQueries is deprecated and doesn't do anything. It will be removed in a future version."
)


class ScalarFormulaRequestQueries:
    def __new__(cls, *args, **kwargs):
        return args[0]
