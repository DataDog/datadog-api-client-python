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
    from datadog_api_client.v2.model.incident_role_assignment_role_relationship import (
        IncidentRoleAssignmentRoleRelationship,
    )
    from datadog_api_client.v2.model.incident_role_assignment_responder_relationship import (
        IncidentRoleAssignmentResponderRelationship,
    )


class IncidentRoleAssignmentRelationshipsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_role_assignment_role_relationship import (
            IncidentRoleAssignmentRoleRelationship,
        )
        from datadog_api_client.v2.model.incident_role_assignment_responder_relationship import (
            IncidentRoleAssignmentResponderRelationship,
        )

        return {
            "reserved_role": (IncidentRoleAssignmentRoleRelationship,),
            "responder": (IncidentRoleAssignmentResponderRelationship,),
            "user_defined_role": (IncidentRoleAssignmentRoleRelationship,),
        }

    attribute_map = {
        "reserved_role": "reserved_role",
        "responder": "responder",
        "user_defined_role": "user_defined_role",
    }

    def __init__(
        self_,
        responder: IncidentRoleAssignmentResponderRelationship,
        reserved_role: Union[IncidentRoleAssignmentRoleRelationship, UnsetType] = unset,
        user_defined_role: Union[IncidentRoleAssignmentRoleRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships for creating a role assignment.

        :param reserved_role: Relationship to a role.
        :type reserved_role: IncidentRoleAssignmentRoleRelationship, optional

        :param responder: Relationship to a responder.
        :type responder: IncidentRoleAssignmentResponderRelationship

        :param user_defined_role: Relationship to a role.
        :type user_defined_role: IncidentRoleAssignmentRoleRelationship, optional
        """
        if reserved_role is not unset:
            kwargs["reserved_role"] = reserved_role
        if user_defined_role is not unset:
            kwargs["user_defined_role"] = user_defined_role
        super().__init__(kwargs)

        self_.responder = responder
