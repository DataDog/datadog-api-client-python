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
    from datadog_api_client.v2.model.incident_impact_field_data_attributes_response import (
        IncidentImpactFieldDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_impact_field_relationships import IncidentImpactFieldRelationships
    from datadog_api_client.v2.model.incident_impact_field_type import IncidentImpactFieldType


class IncidentImpactFieldDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_field_data_attributes_response import (
            IncidentImpactFieldDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_impact_field_relationships import IncidentImpactFieldRelationships
        from datadog_api_client.v2.model.incident_impact_field_type import IncidentImpactFieldType

        return {
            "attributes": (IncidentImpactFieldDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentImpactFieldRelationships,),
            "type": (IncidentImpactFieldType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentImpactFieldDataAttributesResponse,
        id: UUID,
        type: IncidentImpactFieldType,
        relationships: Union[IncidentImpactFieldRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Impact field data in a response.

        :param attributes: Attributes of an impact field in a response.
        :type attributes: IncidentImpactFieldDataAttributesResponse

        :param id: The impact field identifier.
        :type id: UUID

        :param relationships: Relationships for an impact field.
        :type relationships: IncidentImpactFieldRelationships, optional

        :param type: Impact field resource type.
        :type type: IncidentImpactFieldType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
