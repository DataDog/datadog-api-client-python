import warnings

warnings.warn("SlackIntegrationChannels is deprecated and doesn't do anything. It will be removed in a future version.")


class SlackIntegrationChannels:
    def __new__(cls, *args, **kwargs):
        return args[0]
