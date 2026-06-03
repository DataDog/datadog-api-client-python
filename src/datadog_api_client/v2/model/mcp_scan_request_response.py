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
    from datadog_api_client.v2.model.mcp_scan_request_response_data import McpScanRequestResponseData


class McpScanRequestResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_scan_request_response_data import McpScanRequestResponseData

        return {
            "data": (McpScanRequestResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: McpScanRequestResponseData, **kwargs):
        """
        The top-level response object returned when an MCP SCA dependency scan request has been accepted.

        :param data: The data object returned when a scan request has been accepted.
        :type data: McpScanRequestResponseData
        """
        super().__init__(kwargs)

        self_.data = data
