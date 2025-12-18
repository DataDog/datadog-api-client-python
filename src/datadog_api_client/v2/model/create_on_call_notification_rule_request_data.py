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
    from datadog_api_client.v2.model.on_call_notification_rule_request_attributes import (
        OnCallNotificationRuleRequestAttributes,
    )
    from datadog_api_client.v2.model.on_call_notification_rule_relationships import OnCallNotificationRuleRelationships
    from datadog_api_client.v2.model.on_call_notification_rule_type import OnCallNotificationRuleType


class CreateOnCallNotificationRuleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_notification_rule_request_attributes import (
            OnCallNotificationRuleRequestAttributes,
        )
        from datadog_api_client.v2.model.on_call_notification_rule_relationships import (
            OnCallNotificationRuleRelationships,
        )
        from datadog_api_client.v2.model.on_call_notification_rule_type import OnCallNotificationRuleType

        return {
            "attributes": (OnCallNotificationRuleRequestAttributes,),
            "relationships": (OnCallNotificationRuleRelationships,),
            "type": (OnCallNotificationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: OnCallNotificationRuleType,
        attributes: Union[OnCallNotificationRuleRequestAttributes, UnsetType] = unset,
        relationships: Union[OnCallNotificationRuleRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for creating an on-call notification rule

        :param attributes: Attributes for creating or modifying an on-call notification rule.
        :type attributes: OnCallNotificationRuleRequestAttributes, optional

        :param relationships: Relationship object for creating a notification rule
        :type relationships: OnCallNotificationRuleRelationships, optional

        :param type: Indicates that the resource is of type 'notification_rules'.
        :type type: OnCallNotificationRuleType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
