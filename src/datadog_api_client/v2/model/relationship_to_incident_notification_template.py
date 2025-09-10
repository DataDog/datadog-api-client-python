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
    from datadog_api_client.v2.model.relationship_to_incident_notification_template_data import (
        RelationshipToIncidentNotificationTemplateData,
    )


class RelationshipToIncidentNotificationTemplate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_notification_template_data import (
            RelationshipToIncidentNotificationTemplateData,
        )

        return {
            "data": (RelationshipToIncidentNotificationTemplateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RelationshipToIncidentNotificationTemplateData, **kwargs):
        """
        A relationship reference to a notification template.

        :param data: The notification template relationship data.
        :type data: RelationshipToIncidentNotificationTemplateData
        """
        super().__init__(kwargs)

        self_.data = data
