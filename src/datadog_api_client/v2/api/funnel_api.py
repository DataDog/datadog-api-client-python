# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.funnel_response import FunnelResponse
from datadog_api_client.v2.model.funnel_request import FunnelRequest
from datadog_api_client.v2.model.funnel_suggestion_response import FunnelSuggestionResponse
from datadog_api_client.v2.model.funnel_suggestion_request import FunnelSuggestionRequest


class FunnelApi:
    """
    API for funnel.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_rum_funnel_endpoint = _Endpoint(
            settings={
                "response_type": (FunnelResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/funnel",
                "operation_id": "get_rum_funnel",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FunnelRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_rum_funnel_step_suggestions_endpoint = _Endpoint(
            settings={
                "response_type": (FunnelSuggestionResponse,),
                "auth": [],
                "endpoint_path": "/api/v2/rum/funnel/new_step_suggestions",
                "operation_id": "get_rum_funnel_step_suggestions",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FunnelSuggestionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_rum_funnel(
        self,
        body: FunnelRequest,
    ) -> FunnelResponse:
        """Get rum funnel.

        Analyze conversion funnels to understand user drop-off patterns

        :type body: FunnelRequest
        :rtype: FunnelResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_rum_funnel_endpoint.call_with_http_info(**kwargs)

    def get_rum_funnel_step_suggestions(
        self,
        body: FunnelSuggestionRequest,
    ) -> FunnelSuggestionResponse:
        """Get rum funnel step suggestions.

        Get suggested steps for building conversion funnels

        :type body: FunnelSuggestionRequest
        :rtype: FunnelSuggestionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._get_rum_funnel_step_suggestions_endpoint.call_with_http_info(**kwargs)
