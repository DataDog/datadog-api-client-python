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
    from datadog_api_client.v2.model.incident_role_assignment_responder_relationship import (
        IncidentRoleAssignmentResponderRelationship,
    )
    from datadog_api_client.v2.model.incident_role_assignment_role_relationship import (
        IncidentRoleAssignmentRoleRelationship,
    )


class IncidentRoleAssignmentRelationshipsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_role_assignment_responder_relationship import (
            IncidentRoleAssignmentResponderRelationship,
        )
        from datadog_api_client.v2.model.incident_role_assignment_role_relationship import (
            IncidentRoleAssignmentRoleRelationship,
        )

        return {
            "created_by_user": (IncidentRoleAssignmentResponderRelationship,),
            "last_modified_by_user": (IncidentRoleAssignmentResponderRelationship,),
            "reserved_role": (IncidentRoleAssignmentRoleRelationship,),
            "responder": (IncidentRoleAssignmentResponderRelationship,),
            "user_defined_role": (IncidentRoleAssignmentRoleRelationship,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "last_modified_by_user": "last_modified_by_user",
        "reserved_role": "reserved_role",
        "responder": "responder",
        "user_defined_role": "user_defined_role",
    }

    def __init__(
        self_,
        responder: IncidentRoleAssignmentResponderRelationship,
        created_by_user: Union[IncidentRoleAssignmentResponderRelationship, UnsetType] = unset,
        last_modified_by_user: Union[IncidentRoleAssignmentResponderRelationship, UnsetType] = unset,
        reserved_role: Union[IncidentRoleAssignmentRoleRelationship, UnsetType] = unset,
        user_defined_role: Union[IncidentRoleAssignmentRoleRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of a role assignment.

        :param created_by_user: Relationship to a responder.
        :type created_by_user: IncidentRoleAssignmentResponderRelationship, optional

        :param last_modified_by_user: Relationship to a responder.
        :type last_modified_by_user: IncidentRoleAssignmentResponderRelationship, optional

        :param reserved_role: Relationship to a role.
        :type reserved_role: IncidentRoleAssignmentRoleRelationship, optional

        :param responder: Relationship to a responder.
        :type responder: IncidentRoleAssignmentResponderRelationship

        :param user_defined_role: Relationship to a role.
        :type user_defined_role: IncidentRoleAssignmentRoleRelationship, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if reserved_role is not unset:
            kwargs["reserved_role"] = reserved_role
        if user_defined_role is not unset:
            kwargs["user_defined_role"] = user_defined_role
        super().__init__(kwargs)

        self_.responder = responder
