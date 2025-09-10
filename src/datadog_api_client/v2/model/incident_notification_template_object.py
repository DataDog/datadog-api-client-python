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
    from datadog_api_client.v2.model.incident_notification_template_attributes import (
        IncidentNotificationTemplateAttributes,
    )
    from datadog_api_client.v2.model.incident_notification_template_relationships import (
        IncidentNotificationTemplateRelationships,
    )
    from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType


class IncidentNotificationTemplateObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_template_attributes import (
            IncidentNotificationTemplateAttributes,
        )
        from datadog_api_client.v2.model.incident_notification_template_relationships import (
            IncidentNotificationTemplateRelationships,
        )
        from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType

        return {
            "attributes": (IncidentNotificationTemplateAttributes,),
            "id": (UUID,),
            "relationships": (IncidentNotificationTemplateRelationships,),
            "type": (IncidentNotificationTemplateType,),
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
        type: IncidentNotificationTemplateType,
        attributes: Union[IncidentNotificationTemplateAttributes, UnsetType] = unset,
        relationships: Union[IncidentNotificationTemplateRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A notification template object for inclusion in other resources.

        :param attributes: The notification template's attributes.
        :type attributes: IncidentNotificationTemplateAttributes, optional

        :param id: The unique identifier of the notification template.
        :type id: UUID

        :param relationships: The notification template's resource relationships.
        :type relationships: IncidentNotificationTemplateRelationships, optional

        :param type: Notification templates resource type.
        :type type: IncidentNotificationTemplateType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
