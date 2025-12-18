# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class OnCallNotificationRulesIncluded(ModelComposed):
    def __init__(self, **kwargs):
        """
        Represents additional included resources for a on-call notification rules

        :param attributes: Attributes for an on-call notification channel.
        :type attributes: NotificationChannelAttributes, optional

        :param id: Unique identifier for the channel
        :type id: str, optional

        :param type: Indicates that the resource is of type 'notification_channels'.
        :type type: NotificationChannelType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.notification_channel_data import NotificationChannelData

        return {
            "oneOf": [
                NotificationChannelData,
            ],
        }
