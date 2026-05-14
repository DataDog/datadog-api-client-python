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
    from datadog_api_client.v2.model.incident_role_assignment_role_relationship_data import (
        IncidentRoleAssignmentRoleRelationshipData,
    )


class IncidentRoleAssignmentRoleRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_role_assignment_role_relationship_data import (
            IncidentRoleAssignmentRoleRelationshipData,
        )

        return {
            "data": (IncidentRoleAssignmentRoleRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[IncidentRoleAssignmentRoleRelationshipData, UnsetType] = unset, **kwargs):
        """
        Relationship to a role.

        :param data: Role relationship data.
        :type data: IncidentRoleAssignmentRoleRelationshipData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
