# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_notification_rule_channel_relationship import (
        OnCallNotificationRuleChannelRelationship,
    )


class OnCallNotificationRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_notification_rule_channel_relationship import (
            OnCallNotificationRuleChannelRelationship,
        )

        return {
            "channel": (OnCallNotificationRuleChannelRelationship,),
        }

    attribute_map = {
        "channel": "channel",
    }

    def __init__(self_, channel: Union[OnCallNotificationRuleChannelRelationship, UnsetType] = unset, **kwargs):
        """
        Relationship object for creating a notification rule

        :param channel: Relationship object for creating a notification rule
        :type channel: OnCallNotificationRuleChannelRelationship, optional
        """
        if channel is not unset:
            kwargs["channel"] = channel
        super().__init__(kwargs)
