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
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
    from datadog_api_client.v2.model.relationship_to_incident_notification_template import (
        RelationshipToIncidentNotificationTemplate,
    )


class IncidentNotificationRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType
        from datadog_api_client.v2.model.relationship_to_incident_notification_template import (
            RelationshipToIncidentNotificationTemplate,
        )

        return {
            "created_by_user": (RelationshipToUser,),
            "incident_type": (RelationshipToIncidentType,),
            "last_modified_by_user": (RelationshipToUser,),
            "notification_template": (RelationshipToIncidentNotificationTemplate,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "incident_type": "incident_type",
        "last_modified_by_user": "last_modified_by_user",
        "notification_template": "notification_template",
    }

    def __init__(
        self_,
        created_by_user: Union[RelationshipToUser, UnsetType] = unset,
        incident_type: Union[RelationshipToIncidentType, UnsetType] = unset,
        last_modified_by_user: Union[RelationshipToUser, UnsetType] = unset,
        notification_template: Union[RelationshipToIncidentNotificationTemplate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The notification rule's resource relationships.

        :param created_by_user: Relationship to user.
        :type created_by_user: RelationshipToUser, optional

        :param incident_type: Relationship to an incident type.
        :type incident_type: RelationshipToIncidentType, optional

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser, optional

        :param notification_template: A relationship reference to a notification template.
        :type notification_template: RelationshipToIncidentNotificationTemplate, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if notification_template is not unset:
            kwargs["notification_template"] = notification_template
        super().__init__(kwargs)
