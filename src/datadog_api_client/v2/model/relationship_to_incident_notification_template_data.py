# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType


class RelationshipToIncidentNotificationTemplateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType

        return {
            "id": (UUID,),
            "type": (IncidentNotificationTemplateType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: IncidentNotificationTemplateType, **kwargs):
        """
        The notification template relationship data.

        :param id: The unique identifier of the notification template.
        :type id: UUID

        :param type: Notification templates resource type.
        :type type: IncidentNotificationTemplateType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
