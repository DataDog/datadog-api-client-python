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
    from datadog_api_client.v1.model.sankey_network_query import SankeyNetworkQuery
    from datadog_api_client.v1.model.sankey_network_request_type import SankeyNetworkRequestType


class SankeyNetworkRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.sankey_network_query import SankeyNetworkQuery
        from datadog_api_client.v1.model.sankey_network_request_type import SankeyNetworkRequestType

        return {
            "query": (SankeyNetworkQuery,),
            "request_type": (SankeyNetworkRequestType,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(self_, query: SankeyNetworkQuery, request_type: SankeyNetworkRequestType, **kwargs):
        """
        Sankey widget request for network data source.

        :param query: Query configuration for Sankey network widget.
        :type query: SankeyNetworkQuery

        :param request_type: Type of request for network Sankey widget.
        :type request_type: SankeyNetworkRequestType
        """
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
