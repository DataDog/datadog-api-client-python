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
    from datadog_api_client.v2.model.incident_user_defined_role_data_attributes_request import (
        IncidentUserDefinedRoleDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_user_defined_role_relationships_request import (
        IncidentUserDefinedRoleRelationshipsRequest,
    )
    from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType


class IncidentUserDefinedRoleDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_data_attributes_request import (
            IncidentUserDefinedRoleDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_user_defined_role_relationships_request import (
            IncidentUserDefinedRoleRelationshipsRequest,
        )
        from datadog_api_client.v2.model.incident_user_defined_role_type import IncidentUserDefinedRoleType

        return {
            "attributes": (IncidentUserDefinedRoleDataAttributesRequest,),
            "relationships": (IncidentUserDefinedRoleRelationshipsRequest,),
            "type": (IncidentUserDefinedRoleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentUserDefinedRoleDataAttributesRequest,
        relationships: IncidentUserDefinedRoleRelationshipsRequest,
        type: IncidentUserDefinedRoleType,
        **kwargs,
    ):
        """
        Data for creating an incident user-defined role.

        :param attributes: Attributes for creating an incident user-defined role.
        :type attributes: IncidentUserDefinedRoleDataAttributesRequest

        :param relationships: Relationships for creating a user-defined role.
        :type relationships: IncidentUserDefinedRoleRelationshipsRequest

        :param type: Incident user-defined role resource type.
        :type type: IncidentUserDefinedRoleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
