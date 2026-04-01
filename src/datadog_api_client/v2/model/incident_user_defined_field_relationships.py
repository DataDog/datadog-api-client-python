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
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType


class IncidentUserDefinedFieldRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType

        return {
            "created_by_user": (RelationshipToUser,),
            "incident_type": (RelationshipToIncidentType,),
            "last_modified_by_user": (RelationshipToUser,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "incident_type": "incident_type",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        created_by_user: RelationshipToUser,
        incident_type: RelationshipToIncidentType,
        last_modified_by_user: RelationshipToUser,
        **kwargs,
    ):
        """
        Relationships of an incident user-defined field.

        :param created_by_user: Relationship to user.
        :type created_by_user: RelationshipToUser

        :param incident_type: Relationship to an incident type.
        :type incident_type: RelationshipToIncidentType

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser
        """
        super().__init__(kwargs)

        self_.created_by_user = created_by_user
        self_.incident_type = incident_type
        self_.last_modified_by_user = last_modified_by_user
