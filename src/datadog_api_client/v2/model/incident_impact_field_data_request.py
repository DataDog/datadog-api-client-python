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
    from datadog_api_client.v2.model.incident_impact_field_data_attributes_request import (
        IncidentImpactFieldDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_impact_field_relationships_request import (
        IncidentImpactFieldRelationshipsRequest,
    )
    from datadog_api_client.v2.model.incident_impact_field_type import IncidentImpactFieldType


class IncidentImpactFieldDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_field_data_attributes_request import (
            IncidentImpactFieldDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_impact_field_relationships_request import (
            IncidentImpactFieldRelationshipsRequest,
        )
        from datadog_api_client.v2.model.incident_impact_field_type import IncidentImpactFieldType

        return {
            "attributes": (IncidentImpactFieldDataAttributesRequest,),
            "relationships": (IncidentImpactFieldRelationshipsRequest,),
            "type": (IncidentImpactFieldType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentImpactFieldDataAttributesRequest,
        relationships: IncidentImpactFieldRelationshipsRequest,
        type: IncidentImpactFieldType,
        **kwargs,
    ):
        """
        Impact field data in a create request.

        :param attributes: Attributes for creating an impact field.
        :type attributes: IncidentImpactFieldDataAttributesRequest

        :param relationships: Relationships for an impact field create request.
        :type relationships: IncidentImpactFieldRelationshipsRequest

        :param type: Impact field resource type.
        :type type: IncidentImpactFieldType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
