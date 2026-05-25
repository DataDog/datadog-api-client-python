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
    from datadog_api_client.v2.model.node_types_response_data_attributes import NodeTypesResponseDataAttributes
    from datadog_api_client.v2.model.node_types_response_data_type import NodeTypesResponseDataType


class NodeTypesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.node_types_response_data_attributes import NodeTypesResponseDataAttributes
        from datadog_api_client.v2.model.node_types_response_data_type import NodeTypesResponseDataType

        return {
            "attributes": (NodeTypesResponseDataAttributes,),
            "id": (str,),
            "type": (NodeTypesResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: NodeTypesResponseDataAttributes, id: str, type: NodeTypesResponseDataType, **kwargs
    ):
        """
        The primary data object in the node types response.

        :param attributes: The attributes of the node types response, containing the list of node type definitions for the requested language.
        :type attributes: NodeTypesResponseDataAttributes

        :param id: The unique identifier of the node types response resource.
        :type id: str

        :param type: Get node types response resource type.
        :type type: NodeTypesResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
