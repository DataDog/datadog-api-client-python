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
    from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
    from datadog_api_client.v2.model.relationship_to_incident_notification_template import (
        RelationshipToIncidentNotificationTemplate,
    )


class IncidentNotificationRuleCreateDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
        from datadog_api_client.v2.model.relationship_to_incident_notification_template import (
            RelationshipToIncidentNotificationTemplate,
        )

        return {
            "incident_type": (RelationshipToIncidentType,),
            "notification_template": (RelationshipToIncidentNotificationTemplate,),
        }

    attribute_map = {
        "incident_type": "incident_type",
        "notification_template": "notification_template",
    }

    def __init__(
        self_,
        incident_type: Union[RelationshipToIncidentType, UnsetType] = unset,
        notification_template: Union[RelationshipToIncidentNotificationTemplate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``NotificationRuleCreateDataRelationships`` object.

        :param incident_type: Relationship to an incident type.
        :type incident_type: RelationshipToIncidentType, optional

        :param notification_template: A relationship reference to a notification template.
        :type notification_template: RelationshipToIncidentNotificationTemplate, optional
        """
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        if notification_template is not unset:
            kwargs["notification_template"] = notification_template
        super().__init__(kwargs)
