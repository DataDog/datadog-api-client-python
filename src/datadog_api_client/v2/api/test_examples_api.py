# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.test_examples_response import TestExamplesResponse


class TestExamplesApi:
    """
    Manage test example resources.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_test_examples_endpoint = _Endpoint(
            settings={
                "response_type": (TestExamplesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/test-examples",
                "operation_id": "list_test_examples",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_test_examples(
        self,
    ) -> TestExamplesResponse:
        """List test examples.

        Get a list of all test examples.

        :rtype: TestExamplesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_test_examples_endpoint.call_with_http_info(**kwargs)
