# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.slack_integration_channel_display import SlackIntegrationChannelDisplay

    globals()["SlackIntegrationChannelDisplay"] = SlackIntegrationChannelDisplay


class SlackIntegrationChannel(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "display": (SlackIntegrationChannelDisplay,),
            "name": (str,),
        }

    attribute_map = {
        "display": "display",
        "name": "name",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        The Slack channel configuration.

        :param display: Configuration options for what is shown in an alert event message.
        :type display: SlackIntegrationChannelDisplay, optional

        :param name: Your channel name.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SlackIntegrationChannel, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
