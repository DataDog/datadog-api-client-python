# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.incident_responder_role_assignments_relationship import (
        IncidentResponderRoleAssignmentsRelationship,
    )
    from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser


class IncidentResponderRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.incident_responder_role_assignments_relationship import (
            IncidentResponderRoleAssignmentsRelationship,
        )
        from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser

        return {
            "created_by": (RelationshipToUser,),
            "last_modified_by": (RelationshipToUser,),
            "role_assignments": (IncidentResponderRoleAssignmentsRelationship,),
            "user": (NullableRelationshipToUser,),
        }

    attribute_map = {
        "created_by": "created_by",
        "last_modified_by": "last_modified_by",
        "role_assignments": "role_assignments",
        "user": "user",
    }

    def __init__(
        self_,
        created_by: Union[RelationshipToUser, UnsetType] = unset,
        last_modified_by: Union[RelationshipToUser, UnsetType] = unset,
        role_assignments: Union[IncidentResponderRoleAssignmentsRelationship, UnsetType] = unset,
        user: Union[NullableRelationshipToUser, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships for an incident responder.

        :param created_by: Relationship to user.
        :type created_by: RelationshipToUser, optional

        :param last_modified_by: Relationship to user.
        :type last_modified_by: RelationshipToUser, optional

        :param role_assignments: Relationship to role assignments for a responder.
        :type role_assignments: IncidentResponderRoleAssignmentsRelationship, optional

        :param user: Relationship to user.
        :type user: NullableRelationshipToUser, none_type, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if last_modified_by is not unset:
            kwargs["last_modified_by"] = last_modified_by
        if role_assignments is not unset:
            kwargs["role_assignments"] = role_assignments
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
