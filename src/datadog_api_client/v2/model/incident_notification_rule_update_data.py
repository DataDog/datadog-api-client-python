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
    from datadog_api_client.v2.model.incident_notification_rule_create_attributes import (
        IncidentNotificationRuleCreateAttributes,
    )
    from datadog_api_client.v2.model.incident_notification_rule_create_data_relationships import (
        IncidentNotificationRuleCreateDataRelationships,
    )
    from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType


class IncidentNotificationRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_rule_create_attributes import (
            IncidentNotificationRuleCreateAttributes,
        )
        from datadog_api_client.v2.model.incident_notification_rule_create_data_relationships import (
            IncidentNotificationRuleCreateDataRelationships,
        )
        from datadog_api_client.v2.model.incident_notification_rule_type import IncidentNotificationRuleType

        return {
            "attributes": (IncidentNotificationRuleCreateAttributes,),
            "id": (UUID,),
            "relationships": (IncidentNotificationRuleCreateDataRelationships,),
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
        attributes: IncidentNotificationRuleCreateAttributes,
        id: UUID,
        type: IncidentNotificationRuleType,
        relationships: Union[IncidentNotificationRuleCreateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification rule data for an update request.

        :param attributes: The attributes for creating a notification rule.
        :type attributes: IncidentNotificationRuleCreateAttributes

        :param id: The unique identifier of the notification rule.
        :type id: UUID

        :param relationships: The definition of ``NotificationRuleCreateDataRelationships`` object.
        :type relationships: IncidentNotificationRuleCreateDataRelationships, optional

        :param type: Notification rules resource type.
        :type type: IncidentNotificationRuleType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
