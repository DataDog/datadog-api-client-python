# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.sca_request import ScaRequest
from datadog_api_client.v2.model.resolve_vulnerable_symbols_response import ResolveVulnerableSymbolsResponse
from datadog_api_client.v2.model.resolve_vulnerable_symbols_request import ResolveVulnerableSymbolsRequest


class StaticAnalysisApi:
    """
    API for static analysis
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_sca_resolve_vulnerable_symbols_endpoint = _Endpoint(
            settings={
                "response_type": (ResolveVulnerableSymbolsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis-sca/vulnerabilities/resolve-vulnerable-symbols",
                "operation_id": "create_sca_resolve_vulnerable_symbols",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ResolveVulnerableSymbolsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_sca_result_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/static-analysis-sca/dependencies",
                "operation_id": "create_sca_result",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ScaRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_sca_resolve_vulnerable_symbols(
        self,
        body: ResolveVulnerableSymbolsRequest,
    ) -> ResolveVulnerableSymbolsResponse:
        """POST request to resolve vulnerable symbols.

        :type body: ResolveVulnerableSymbolsRequest
        :rtype: ResolveVulnerableSymbolsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_sca_resolve_vulnerable_symbols_endpoint.call_with_http_info(**kwargs)

    def create_sca_result(
        self,
        body: ScaRequest,
    ) -> None:
        """Post dependencies for analysis.

        :type body: ScaRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_sca_result_endpoint.call_with_http_info(**kwargs)
