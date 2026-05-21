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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_role_assignment_data_attributes_response import (
        IncidentRoleAssignmentDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_role_assignment_relationships_response import (
        IncidentRoleAssignmentRelationshipsResponse,
    )
    from datadog_api_client.v2.model.incident_role_assignment_type import IncidentRoleAssignmentType


class IncidentRoleAssignmentDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_role_assignment_data_attributes_response import (
            IncidentRoleAssignmentDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_role_assignment_relationships_response import (
            IncidentRoleAssignmentRelationshipsResponse,
        )
        from datadog_api_client.v2.model.incident_role_assignment_type import IncidentRoleAssignmentType

        return {
            "attributes": (IncidentRoleAssignmentDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentRoleAssignmentRelationshipsResponse,),
            "type": (IncidentRoleAssignmentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentRoleAssignmentDataAttributesResponse,
        id: UUID,
        type: IncidentRoleAssignmentType,
        relationships: Union[IncidentRoleAssignmentRelationshipsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Role assignment data in a response.

        :param attributes: Attributes of an incident role assignment.
        :type attributes: IncidentRoleAssignmentDataAttributesResponse

        :param id: The role assignment identifier.
        :type id: UUID

        :param relationships: Relationships of a role assignment.
        :type relationships: IncidentRoleAssignmentRelationshipsResponse, optional

        :param type: Incident role assignment resource type.
        :type type: IncidentRoleAssignmentType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
