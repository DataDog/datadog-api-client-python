# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.flaky_tests_search_response import FlakyTestsSearchResponse
from datadog_api_client.v2.model.flaky_tests_search_request import FlakyTestsSearchRequest
from datadog_api_client.v2.model.flaky_test import FlakyTest


class TestOptimizationApi:
    """
    Search and manage flaky tests through Test Optimization. See the `Test Optimization page <https://docs.datadoghq.com/tests/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._search_flaky_tests_endpoint = _Endpoint(
            settings={
                "response_type": (FlakyTestsSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/test/flaky-test-management/tests",
                "operation_id": "search_flaky_tests",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "openapi_types": (FlakyTestsSearchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def search_flaky_tests(
        self,
        *,
        body: Union[FlakyTestsSearchRequest, UnsetType] = unset,
    ) -> FlakyTestsSearchResponse:
        """Search flaky tests.

        List endpoint returning flaky tests from Flaky Test Management. Results are paginated.

        :type body: FlakyTestsSearchRequest, optional
        :rtype: FlakyTestsSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._search_flaky_tests_endpoint.call_with_http_info(**kwargs)

    def search_flaky_tests_with_pagination(
        self,
        *,
        body: Union[FlakyTestsSearchRequest, UnsetType] = unset,
    ) -> collections.abc.Iterable[FlakyTest]:
        """Search flaky tests.

        Provide a paginated version of :meth:`search_flaky_tests`, returning all items.

        :type body: FlakyTestsSearchRequest, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[FlakyTest]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.data.attributes.page.limit", 10)
        endpoint = self._search_flaky_tests_endpoint
        set_attribute_from_path(kwargs, "body.data.attributes.page.limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "body.data.attributes.page.cursor",
            "cursor_path": "meta.pagination.next_page",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
