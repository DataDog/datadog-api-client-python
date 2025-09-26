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
    from datadog_api_client.v2.model.incident_impact_attributes import IncidentImpactAttributes
    from datadog_api_client.v2.model.incident_impact_relationships import IncidentImpactRelationships
    from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType


class IncidentImpactResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_attributes import IncidentImpactAttributes
        from datadog_api_client.v2.model.incident_impact_relationships import IncidentImpactRelationships
        from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType

        return {
            "attributes": (IncidentImpactAttributes,),
            "id": (str,),
            "relationships": (IncidentImpactRelationships,),
            "type": (IncidentImpactType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: IncidentImpactType,
        attributes: Union[IncidentImpactAttributes, UnsetType] = unset,
        relationships: Union[IncidentImpactRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident impact data from a response.

        :param attributes: The incident impact's attributes.
        :type attributes: IncidentImpactAttributes, optional

        :param id: The incident impact's ID.
        :type id: str

        :param relationships: The incident impact's resource relationships.
        :type relationships: IncidentImpactRelationships, optional

        :param type: Incident impact resource type.
        :type type: IncidentImpactType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
