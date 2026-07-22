# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.pup_bump_test_response import PupBumpTestResponse


class PupBumpTestApi:
    """
    Temporary test-only tag used to exercise the pup dependency-bump
    generation and merge pipeline. Not a real product feature.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_pup_bump_test_endpoint = _Endpoint(
            settings={
                "response_type": (PupBumpTestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/pup_bump_test",
                "operation_id": "get_pup_bump_test",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_pup_bump_test(
        self,
    ) -> PupBumpTestResponse:
        """Get pup bump test resource.

        Temporary test-only endpoint used to exercise the pup dependency-bump
        generation and merge pipeline. Not a real product feature.

        :rtype: PupBumpTestResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_pup_bump_test_endpoint.call_with_http_info(**kwargs)
