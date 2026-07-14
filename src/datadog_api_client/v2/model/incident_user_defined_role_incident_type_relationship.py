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
    from datadog_api_client.v2.model.incident_user_defined_role_incident_type_relationship_data import (
        IncidentUserDefinedRoleIncidentTypeRelationshipData,
    )


class IncidentUserDefinedRoleIncidentTypeRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_incident_type_relationship_data import (
            IncidentUserDefinedRoleIncidentTypeRelationshipData,
        )

        return {
            "data": (IncidentUserDefinedRoleIncidentTypeRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IncidentUserDefinedRoleIncidentTypeRelationshipData, **kwargs):
        """
        Relationship to an incident type for a user-defined role.

        :param data: Data for the incident type relationship of a user-defined role.
        :type data: IncidentUserDefinedRoleIncidentTypeRelationshipData
        """
        super().__init__(kwargs)

        self_.data = data
