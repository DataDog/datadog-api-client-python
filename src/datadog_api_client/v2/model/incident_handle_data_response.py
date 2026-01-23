# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_handle_attributes_response import IncidentHandleAttributesResponse
    from datadog_api_client.v2.model.incident_handle_relationships import IncidentHandleRelationships
    from datadog_api_client.v2.model.incident_handle_type import IncidentHandleType


class IncidentHandleDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_handle_attributes_response import IncidentHandleAttributesResponse
        from datadog_api_client.v2.model.incident_handle_relationships import IncidentHandleRelationships
        from datadog_api_client.v2.model.incident_handle_type import IncidentHandleType

        return {
            "attributes": (IncidentHandleAttributesResponse,),
            "id": (str,),
            "relationships": (IncidentHandleRelationships,),
            "type": (IncidentHandleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentHandleAttributesResponse,
        id: str,
        type: IncidentHandleType,
        relationships: Union[IncidentHandleRelationships, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: Incident handle attributes for responses
        :type attributes: IncidentHandleAttributesResponse

        :param id: The ID of the incident handle
        :type id: str

        :param relationships:
        :type relationships: IncidentHandleRelationships, none_type, optional

        :param type: Incident handle resource type
        :type type: IncidentHandleType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
