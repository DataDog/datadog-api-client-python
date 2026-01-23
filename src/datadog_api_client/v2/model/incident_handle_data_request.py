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
    from datadog_api_client.v2.model.incident_handle_attributes_request import IncidentHandleAttributesRequest
    from datadog_api_client.v2.model.incident_handle_relationships_request import IncidentHandleRelationshipsRequest
    from datadog_api_client.v2.model.incident_handle_type import IncidentHandleType


class IncidentHandleDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_handle_attributes_request import IncidentHandleAttributesRequest
        from datadog_api_client.v2.model.incident_handle_relationships_request import IncidentHandleRelationshipsRequest
        from datadog_api_client.v2.model.incident_handle_type import IncidentHandleType

        return {
            "attributes": (IncidentHandleAttributesRequest,),
            "id": (str,),
            "relationships": (IncidentHandleRelationshipsRequest,),
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
        attributes: IncidentHandleAttributesRequest,
        type: IncidentHandleType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[IncidentHandleRelationshipsRequest, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: Incident handle attributes for requests
        :type attributes: IncidentHandleAttributesRequest

        :param id: The ID of the incident handle (required for PUT requests)
        :type id: str, optional

        :param relationships:
        :type relationships: IncidentHandleRelationshipsRequest, none_type, optional

        :param type: Incident handle resource type
        :type type: IncidentHandleType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
