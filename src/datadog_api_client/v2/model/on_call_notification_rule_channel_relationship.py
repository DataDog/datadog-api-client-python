# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_notification_rule_channel_relationship_data import (
        OnCallNotificationRuleChannelRelationshipData,
    )


class OnCallNotificationRuleChannelRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_notification_rule_channel_relationship_data import (
            OnCallNotificationRuleChannelRelationshipData,
        )

        return {
            "data": (OnCallNotificationRuleChannelRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OnCallNotificationRuleChannelRelationshipData, **kwargs):
        """
        Relationship object for creating a notification rule

        :param data: Channel relationship data for creating a notification rule
        :type data: OnCallNotificationRuleChannelRelationshipData
        """
        super().__init__(kwargs)

        self_.data = data
