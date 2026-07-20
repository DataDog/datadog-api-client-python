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
    from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_data import (
        McpCrossAppAccessIssuerUrlUpdateData,
    )


class McpCrossAppAccessIssuerUrlUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_data import (
            McpCrossAppAccessIssuerUrlUpdateData,
        )

        return {
            "data": (McpCrossAppAccessIssuerUrlUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: McpCrossAppAccessIssuerUrlUpdateData, **kwargs):
        """
        A request to update the MCP Cross-App Access issuer URL for an organization.

        :param data: The data object for an MCP Cross-App Access issuer URL update request.
        :type data: McpCrossAppAccessIssuerUrlUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
