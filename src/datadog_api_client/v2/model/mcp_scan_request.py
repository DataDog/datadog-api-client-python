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
    from datadog_api_client.v2.model.mcp_scan_request_data import McpScanRequestData


class McpScanRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_scan_request_data import McpScanRequestData

        return {
            "data": (McpScanRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: McpScanRequestData, **kwargs):
        """
        The top-level request object for submitting an MCP SCA dependency scan.

        :param data: The data object in an MCP SCA scan request, containing the scan attributes and request type.
        :type data: McpScanRequestData
        """
        super().__init__(kwargs)

        self_.data = data
