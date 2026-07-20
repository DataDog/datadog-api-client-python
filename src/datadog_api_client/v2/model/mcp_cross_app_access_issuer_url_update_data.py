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
    from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_attributes import (
        McpCrossAppAccessIssuerUrlUpdateAttributes,
    )
    from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_type import McpCrossAppAccessIssuerUrlType


class McpCrossAppAccessIssuerUrlUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_attributes import (
            McpCrossAppAccessIssuerUrlUpdateAttributes,
        )
        from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_type import McpCrossAppAccessIssuerUrlType

        return {
            "attributes": (McpCrossAppAccessIssuerUrlUpdateAttributes,),
            "type": (McpCrossAppAccessIssuerUrlType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: McpCrossAppAccessIssuerUrlUpdateAttributes, type: McpCrossAppAccessIssuerUrlType, **kwargs
    ):
        """
        The data object for an MCP Cross-App Access issuer URL update request.

        :param attributes: Attributes for the MCP Cross-App Access issuer URL update request.
        :type attributes: McpCrossAppAccessIssuerUrlUpdateAttributes

        :param type: Data type of an MCP Cross-App Access issuer URL update.
        :type type: McpCrossAppAccessIssuerUrlType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
