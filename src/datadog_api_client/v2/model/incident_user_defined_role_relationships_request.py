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
    from datadog_api_client.v2.model.incident_user_defined_role_incident_type_relationship import (
        IncidentUserDefinedRoleIncidentTypeRelationship,
    )


class IncidentUserDefinedRoleRelationshipsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_incident_type_relationship import (
            IncidentUserDefinedRoleIncidentTypeRelationship,
        )

        return {
            "incident_type": (IncidentUserDefinedRoleIncidentTypeRelationship,),
        }

    attribute_map = {
        "incident_type": "incident_type",
    }

    def __init__(self_, incident_type: IncidentUserDefinedRoleIncidentTypeRelationship, **kwargs):
        """
        Relationships for creating a user-defined role.

        :param incident_type: Relationship to an incident type for a user-defined role.
        :type incident_type: IncidentUserDefinedRoleIncidentTypeRelationship
        """
        super().__init__(kwargs)

        self_.incident_type = incident_type
