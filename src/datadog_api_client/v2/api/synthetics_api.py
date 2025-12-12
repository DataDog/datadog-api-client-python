# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.on_demand_concurrency_cap_response import OnDemandConcurrencyCapResponse
from datadog_api_client.v2.model.on_demand_concurrency_cap_attributes import OnDemandConcurrencyCapAttributes
from datadog_api_client.v2.model.synthetics_suite_response import SyntheticsSuiteResponse
from datadog_api_client.v2.model.suite_create_edit_request import SuiteCreateEditRequest
from datadog_api_client.v2.model.deleted_suites_response import DeletedSuitesResponse
from datadog_api_client.v2.model.deleted_suites_request_delete_request import DeletedSuitesRequestDeleteRequest
from datadog_api_client.v2.model.synthetics_suite_search_response import SyntheticsSuiteSearchResponse


class SyntheticsApi:
    """
    Datadog Synthetics uses simulated user requests and browser rendering to help you ensure uptime,
    identify regional issues, and track your application performance. Datadog Synthetics tests come in
    two different flavors, `API tests <https://docs.datadoghq.com/synthetics/api_tests/>`_
    and `browser tests <https://docs.datadoghq.com/synthetics/browser_tests>`_. You can use Datadog’s API to
    manage both test types programmatically.

    For more information about Synthetics, see the `Synthetics overview <https://docs.datadoghq.com/synthetics/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_synthetics_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites",
                "operation_id": "create_synthetics_suite",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SuiteCreateEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_synthetics_suites_endpoint = _Endpoint(
            settings={
                "response_type": (DeletedSuitesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/bulk-delete",
                "operation_id": "delete_synthetics_suites",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DeletedSuitesRequestDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_synthetics_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/{public_id}",
                "operation_id": "edit_synthetics_suite",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SuiteCreateEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_on_demand_concurrency_cap_endpoint = _Endpoint(
            settings={
                "response_type": (OnDemandConcurrencyCapResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/settings/on_demand_concurrency_cap",
                "operation_id": "get_on_demand_concurrency_cap",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/{public_id}",
                "operation_id": "get_synthetics_suite",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_suites_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/search",
                "operation_id": "search_suites",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "facets_only": {
                    "openapi_types": (bool,),
                    "attribute": "facets_only",
                    "location": "query",
                },
                "start": {
                    "openapi_types": (int,),
                    "attribute": "start",
                    "location": "query",
                },
                "count": {
                    "openapi_types": (int,),
                    "attribute": "count",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._set_on_demand_concurrency_cap_endpoint = _Endpoint(
            settings={
                "response_type": (OnDemandConcurrencyCapResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/settings/on_demand_concurrency_cap",
                "operation_id": "set_on_demand_concurrency_cap",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OnDemandConcurrencyCapAttributes,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_synthetics_suite(
        self,
        body: SuiteCreateEditRequest,
    ) -> SyntheticsSuiteResponse:
        """Synthetics: Create a test suite.

        :type body: SuiteCreateEditRequest
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_synthetics_suite_endpoint.call_with_http_info(**kwargs)

    def delete_synthetics_suites(
        self,
        body: DeletedSuitesRequestDeleteRequest,
    ) -> DeletedSuitesResponse:
        """Synthetics: Bulk delete suites.

        :type body: DeletedSuitesRequestDeleteRequest
        :rtype: DeletedSuitesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_synthetics_suites_endpoint.call_with_http_info(**kwargs)

    def edit_synthetics_suite(
        self,
        public_id: str,
        body: SuiteCreateEditRequest,
    ) -> SyntheticsSuiteResponse:
        """Synthetics: edit a test suite.

        :param public_id: The public ID of the suite to edit.
        :type public_id: str
        :param body: New suite details to be saved.
        :type body: SuiteCreateEditRequest
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._edit_synthetics_suite_endpoint.call_with_http_info(**kwargs)

    def get_on_demand_concurrency_cap(
        self,
    ) -> OnDemandConcurrencyCapResponse:
        """Get the on-demand concurrency cap.

        Get the on-demand concurrency cap.

        :rtype: OnDemandConcurrencyCapResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_on_demand_concurrency_cap_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_suite(
        self,
        public_id: str,
    ) -> SyntheticsSuiteResponse:
        """Synthetics: Get a suite.

        :param public_id: The public ID of the suite to get details from.
        :type public_id: str
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        return self._get_synthetics_suite_endpoint.call_with_http_info(**kwargs)

    def search_suites(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        facets_only: Union[bool, UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
        count: Union[int, UnsetType] = unset,
    ) -> SyntheticsSuiteSearchResponse:
        """Search Synthetics suites.

        Search for Synthetics suites.

        :param query: The search query.
        :type query: str, optional
        :param sort: The sort order for the results (e.g., ``name,asc`` or ``name,desc`` ).
        :type sort: str, optional
        :param facets_only: If true, return only facets instead of full test details.
        :type facets_only: bool, optional
        :param start: The offset from which to start returning results.
        :type start: int, optional
        :param count: The maximum number of results to return.
        :type count: int, optional
        :rtype: SyntheticsSuiteSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if facets_only is not unset:
            kwargs["facets_only"] = facets_only

        if start is not unset:
            kwargs["start"] = start

        if count is not unset:
            kwargs["count"] = count

        return self._search_suites_endpoint.call_with_http_info(**kwargs)

    def set_on_demand_concurrency_cap(
        self,
        body: OnDemandConcurrencyCapAttributes,
    ) -> OnDemandConcurrencyCapResponse:
        """Save new value for on-demand concurrency cap.

        Save new value for on-demand concurrency cap.

        :param body: .
        :type body: OnDemandConcurrencyCapAttributes
        :rtype: OnDemandConcurrencyCapResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._set_on_demand_concurrency_cap_endpoint.call_with_http_info(**kwargs)
