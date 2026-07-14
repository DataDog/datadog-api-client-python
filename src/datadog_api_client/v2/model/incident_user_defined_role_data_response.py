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
    from datadog_api_client.v2.model.incident_user_defined_role_data_attributes_response import (
        IncidentUserDefinedRoleDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_user_defined_role_relationships_response import (
        IncidentUserDefinedRoleRelationshipsResponse,
    )
    from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType


class IncidentUserDefinedRoleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_data_attributes_response import (
            IncidentUserDefinedRoleDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_user_defined_role_relationships_response import (
            IncidentUserDefinedRoleRelationshipsResponse,
        )
        from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType

        return {
            "attributes": (IncidentUserDefinedRoleDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentUserDefinedRoleRelationshipsResponse,),
            "type": (IncidentUserDefinedRoleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentUserDefinedRoleDataAttributesResponse,
        id: UUID,
        type: IncidentUserDefinedRoleType,
        relationships: Union[IncidentUserDefinedRoleRelationshipsResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for an incident user-defined role response.

        :param attributes: Attributes of an incident user-defined role.
        :type attributes: IncidentUserDefinedRoleDataAttributesResponse

        :param id: The ID of the user-defined role.
        :type id: UUID

        :param relationships: Relationships of a user-defined role response.
        :type relationships: IncidentUserDefinedRoleRelationshipsResponse, optional

        :param type: Incident user-defined role resource type.
        :type type: IncidentUserDefinedRoleType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
