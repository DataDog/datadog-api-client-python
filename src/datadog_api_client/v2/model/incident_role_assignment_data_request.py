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
    from datadog_api_client.v2.model.incident_role_assignment_data_attributes_request import (
        IncidentRoleAssignmentDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_role_assignment_relationships_request import (
        IncidentRoleAssignmentRelationshipsRequest,
    )
    from datadog_api_client.v2.model.incident_role_assignment_type import IncidentRoleAssignmentType


class IncidentRoleAssignmentDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_role_assignment_data_attributes_request import (
            IncidentRoleAssignmentDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_role_assignment_relationships_request import (
            IncidentRoleAssignmentRelationshipsRequest,
        )
        from datadog_api_client.v2.model.incident_role_assignment_type import IncidentRoleAssignmentType

        return {
            "attributes": (IncidentRoleAssignmentDataAttributesRequest,),
            "relationships": (IncidentRoleAssignmentRelationshipsRequest,),
            "type": (IncidentRoleAssignmentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        relationships: IncidentRoleAssignmentRelationshipsRequest,
        type: IncidentRoleAssignmentType,
        attributes: Union[IncidentRoleAssignmentDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Role assignment data for a request.

        :param attributes: Attributes for creating a role assignment.
        :type attributes: IncidentRoleAssignmentDataAttributesRequest, optional

        :param relationships: Relationships for creating a role assignment.
        :type relationships: IncidentRoleAssignmentRelationshipsRequest

        :param type: Incident role assignment resource type.
        :type type: IncidentRoleAssignmentType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.relationships = relationships
        self_.type = type
