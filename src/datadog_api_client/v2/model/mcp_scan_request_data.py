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
    from datadog_api_client.v2.model.mcp_scan_request_data_attributes import McpScanRequestDataAttributes
    from datadog_api_client.v2.model.mcp_scan_request_data_type import McpScanRequestDataType


class McpScanRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_scan_request_data_attributes import McpScanRequestDataAttributes
        from datadog_api_client.v2.model.mcp_scan_request_data_type import McpScanRequestDataType

        return {
            "attributes": (McpScanRequestDataAttributes,),
            "id": (str,),
            "type": (McpScanRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: McpScanRequestDataAttributes,
        type: McpScanRequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object in an MCP SCA scan request, containing the scan attributes and request type.

        :param attributes: The attributes of an MCP SCA scan request, describing the libraries to scan and their context.
        :type attributes: McpScanRequestDataAttributes

        :param id: An optional identifier for this scan request.
        :type id: str, optional

        :param type: The type identifier for MCP SCA scan requests.
        :type type: McpScanRequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
