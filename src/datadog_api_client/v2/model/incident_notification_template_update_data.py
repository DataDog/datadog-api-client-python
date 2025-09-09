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
    from datadog_api_client.v2.model.incident_notification_template_update_attributes import (
        IncidentNotificationTemplateUpdateAttributes,
    )
    from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType


class IncidentNotificationTemplateUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_notification_template_update_attributes import (
            IncidentNotificationTemplateUpdateAttributes,
        )
        from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType

        return {
            "attributes": (IncidentNotificationTemplateUpdateAttributes,),
            "id": (UUID,),
            "type": (IncidentNotificationTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: IncidentNotificationTemplateType,
        attributes: Union[IncidentNotificationTemplateUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification template data for an update request.

        :param attributes: The attributes to update on a notification template.
        :type attributes: IncidentNotificationTemplateUpdateAttributes, optional

        :param id: The unique identifier of the notification template.
        :type id: UUID

        :param type: Notification templates resource type.
        :type type: IncidentNotificationTemplateType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
