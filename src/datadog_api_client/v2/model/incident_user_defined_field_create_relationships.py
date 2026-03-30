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
    from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType


class IncidentUserDefinedFieldCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_type import RelationshipToIncidentType

        return {
            "incident_type": (RelationshipToIncidentType,),
        }

    attribute_map = {
        "incident_type": "incident_type",
    }

    def __init__(self_, incident_type: RelationshipToIncidentType, **kwargs):
        """
        Relationships for creating an incident user-defined field.

        :param incident_type: Relationship to an incident type.
        :type incident_type: RelationshipToIncidentType
        """
        super().__init__(kwargs)

        self_.incident_type = incident_type
