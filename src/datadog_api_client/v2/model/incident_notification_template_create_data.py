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
    from datadog_api_client.v2.model.incident_notification_template_create_attributes import (
        IncidentNotificationTemplateCreateAttributes,
    )
    from datadog_api_client.v2.model.incident_notification_template_create_data_relationships import (
        IncidentNotificationTemplateCreateDataRelationships,
    )
    from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType


class IncidentNotificationTemplateCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_template_create_attributes import (
            IncidentNotificationTemplateCreateAttributes,
        )
        from datadog_api_client.v2.model.incident_notification_template_create_data_relationships import (
            IncidentNotificationTemplateCreateDataRelationships,
        )
        from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType

        return {
            "attributes": (IncidentNotificationTemplateCreateAttributes,),
            "relationships": (IncidentNotificationTemplateCreateDataRelationships,),
            "type": (IncidentNotificationTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentNotificationTemplateCreateAttributes,
        type: IncidentNotificationTemplateType,
        relationships: Union[IncidentNotificationTemplateCreateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification template data for a create request.

        :param attributes: The attributes for creating a notification template.
        :type attributes: IncidentNotificationTemplateCreateAttributes

        :param relationships: The definition of ``NotificationTemplateCreateDataRelationships`` object.
        :type relationships: IncidentNotificationTemplateCreateDataRelationships, optional

        :param type: Notification templates resource type.
        :type type: IncidentNotificationTemplateType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
