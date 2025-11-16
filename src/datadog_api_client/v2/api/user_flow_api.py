# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.sankey_response import SankeyResponse
from datadog_api_client.v2.model.sankey_request import SankeyRequest


class UserFlowApi:
    """
    API for user flow.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_rum_sankey_endpoint = _Endpoint(
            settings={
                "response_type": (SankeyResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/sankey",
                "operation_id": "get_rum_sankey",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SankeyRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_rum_sankey(
        self,
        body: SankeyRequest,
    ) -> SankeyResponse:
        """Get rum sankey.

        Generate Sankey diagrams to visualize user flow paths and drop-off points

        :type body: SankeyRequest
        :rtype: SankeyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_rum_sankey_endpoint.call_with_http_info(**kwargs)
