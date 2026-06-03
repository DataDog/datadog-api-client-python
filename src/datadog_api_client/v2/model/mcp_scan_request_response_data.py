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
    from datadog_api_client.v2.model.mcp_scan_request_response_data_attributes import (
        McpScanRequestResponseDataAttributes,
    )
    from datadog_api_client.v2.model.mcp_scan_request_response_data_type import McpScanRequestResponseDataType


class McpScanRequestResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_scan_request_response_data_attributes import (
            McpScanRequestResponseDataAttributes,
        )
        from datadog_api_client.v2.model.mcp_scan_request_response_data_type import McpScanRequestResponseDataType

        return {
            "attributes": (McpScanRequestResponseDataAttributes,),
            "id": (str,),
            "type": (McpScanRequestResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: McpScanRequestResponseDataAttributes, id: str, type: McpScanRequestResponseDataType, **kwargs
    ):
        """
        The data object returned when a scan request has been accepted.

        :param attributes: The attributes returned when a scan request has been accepted, containing the job identifier used to poll for results.
        :type attributes: McpScanRequestResponseDataAttributes

        :param id: The job identifier assigned to the scan.
        :type id: str

        :param type: The type identifier for MCP SCA scan request responses.
        :type type: McpScanRequestResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
