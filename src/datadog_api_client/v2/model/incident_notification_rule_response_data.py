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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_notification_rule_attributes import IncidentNotificationRuleAttributes
    from datadog_api_client.v2.model.incident_notification_rule_relationships import (
        IncidentNotificationRuleRelationships,
    )
    from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType


class IncidentNotificationRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_rule_attributes import IncidentNotificationRuleAttributes
        from datadog_api_client.v2.model.incident_notification_rule_relationships import (
            IncidentNotificationRuleRelationships,
        )
        from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType

        return {
            "attributes": (IncidentNotificationRuleAttributes,),
            "id": (UUID,),
            "relationships": (IncidentNotificationRuleRelationships,),
            "type": (IncidentNotificationRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: IncidentNotificationRuleType,
        attributes: Union[IncidentNotificationRuleAttributes, UnsetType] = unset,
        relationships: Union[IncidentNotificationRuleRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification rule data from a response.

        :param attributes: The notification rule's attributes.
        :type attributes: IncidentNotificationRuleAttributes, optional

        :param id: The unique identifier of the notification rule.
        :type id: UUID

        :param relationships: The notification rule's resource relationships.
        :type relationships: IncidentNotificationRuleRelationships, optional

        :param type: Notification rules resource type.
        :type type: IncidentNotificationRuleType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
