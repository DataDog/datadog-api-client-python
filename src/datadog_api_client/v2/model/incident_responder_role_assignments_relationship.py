# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_responder_role_assignment_relationship_data import (
        IncidentResponderRoleAssignmentRelationshipData,
    )


class IncidentResponderRoleAssignmentsRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responder_role_assignment_relationship_data import (
            IncidentResponderRoleAssignmentRelationshipData,
        )

        return {
            "data": ([IncidentResponderRoleAssignmentRelationshipData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[IncidentResponderRoleAssignmentRelationshipData], UnsetType] = unset, **kwargs
    ):
        """
        Relationship to role assignments for a responder.

        :param data: List of role assignment relationship data.
        :type data: [IncidentResponderRoleAssignmentRelationshipData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
