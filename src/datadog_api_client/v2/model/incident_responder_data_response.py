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
    from datadog_api_client.v2.model.incident_responder_data_attributes_response import (
        IncidentResponderDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_responder_relationships import IncidentResponderRelationships
    from datadog_api_client.v2.model.incident_responder_type import IncidentResponderType


class IncidentResponderDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_responder_data_attributes_response import (
            IncidentResponderDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_responder_relationships import IncidentResponderRelationships
        from datadog_api_client.v2.model.incident_responder_type import IncidentResponderType

        return {
            "attributes": (IncidentResponderDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentResponderRelationships,),
            "type": (IncidentResponderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentResponderDataAttributesResponse,
        id: UUID,
        type: IncidentResponderType,
        relationships: Union[IncidentResponderRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident responder data in a response.

        :param attributes: Attributes of an incident responder in a response.
        :type attributes: IncidentResponderDataAttributesResponse

        :param id: The responder identifier.
        :type id: UUID

        :param relationships: Relationships for an incident responder.
        :type relationships: IncidentResponderRelationships, optional

        :param type: Incident responder resource type.
        :type type: IncidentResponderType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
