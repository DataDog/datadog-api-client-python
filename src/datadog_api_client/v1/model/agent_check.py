import warnings

warnings.warn("AgentCheck is deprecated and doesn't do anything. It will be removed in a future version.")


class AgentCheck:
    def __new__(cls, *args, **kwargs):
        return args[0]
