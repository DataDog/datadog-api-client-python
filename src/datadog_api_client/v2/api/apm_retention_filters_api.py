# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.retention_filters_response import RetentionFiltersResponse
from datadog_api_client.v2.model.retention_filter_create_response import RetentionFilterCreateResponse
from datadog_api_client.v2.model.retention_filter_create_request import RetentionFilterCreateRequest
from datadog_api_client.v2.model.reorder_retention_filters_request import ReorderRetentionFiltersRequest
from datadog_api_client.v2.model.retention_filter_response import RetentionFilterResponse
from datadog_api_client.v2.model.retention_filter_update_request import RetentionFilterUpdateRequest


class APMRetentionFiltersApi:
    """
    Manage configuration of `APM retention filters <https://app.datadoghq.com/apm/traces/retention-filters>`_ for your organization. You need an API and application key with Admin rights to interact with this endpoint. See `retention filters <https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/#retention-filters>`_ on the Trace Retention page for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_apm_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RetentionFilterCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apm/config/retention-filters",
                "operation_id": "create_apm_retention_filter",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RetentionFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_apm_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apm/config/retention-filters/{filter_id}",
                "operation_id": "delete_apm_retention_filter",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_apm_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apm/config/retention-filters/{filter_id}",
                "operation_id": "get_apm_retention_filter",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_apm_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RetentionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apm/config/retention-filters",
                "operation_id": "list_apm_retention_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._reorder_apm_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apm/config/retention-filters-execution-order",
                "operation_id": "reorder_apm_retention_filters",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ReorderRetentionFiltersRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_apm_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/apm/config/retention-filters/{filter_id}",
                "operation_id": "update_apm_retention_filter",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "filter_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RetentionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_apm_retention_filter(
        self,
        body: RetentionFilterCreateRequest,
    ) -> RetentionFilterCreateResponse:
        """Create a retention filter.

        Create a retention filter to index spans in your organization.
        Returns the retention filter definition when the request is successful.

        Default filters with types spans-errors-sampling-processor and spans-appsec-sampling-processor cannot be created.

        :param body: The definition of the new retention filter.
        :type body: RetentionFilterCreateRequest
        :rtype: RetentionFilterCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_apm_retention_filter_endpoint.call_with_http_info(**kwargs)

    def delete_apm_retention_filter(
        self,
        filter_id: str,
    ) -> None:
        """Delete a retention filter.

        Delete a specific retention filter from your organization.

        Default filters with types spans-errors-sampling-processor and spans-appsec-sampling-processor cannot be deleted.

        :param filter_id: The ID of the retention filter.
        :type filter_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_id"] = filter_id

        return self._delete_apm_retention_filter_endpoint.call_with_http_info(**kwargs)

    def get_apm_retention_filter(
        self,
        filter_id: str,
    ) -> RetentionFilterResponse:
        """Get a given APM retention filter.

        Get an APM retention filter.

        :param filter_id: The ID of the retention filter.
        :type filter_id: str
        :rtype: RetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_id"] = filter_id

        return self._get_apm_retention_filter_endpoint.call_with_http_info(**kwargs)

    def list_apm_retention_filters(
        self,
    ) -> RetentionFiltersResponse:
        """List all APM retention filters.

        Get the list of APM retention filters.

        :rtype: RetentionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_apm_retention_filters_endpoint.call_with_http_info(**kwargs)

    def reorder_apm_retention_filters(
        self,
        body: ReorderRetentionFiltersRequest,
    ) -> None:
        """Re-order retention filters.

        Re-order the execution order of retention filters.

        :param body: The list of retention filters in the new order.
        :type body: ReorderRetentionFiltersRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._reorder_apm_retention_filters_endpoint.call_with_http_info(**kwargs)

    def update_apm_retention_filter(
        self,
        filter_id: str,
        body: RetentionFilterUpdateRequest,
    ) -> RetentionFilterResponse:
        """Update a retention filter.

        Update a retention filter from your organization.

        Default filters (filters with types spans-errors-sampling-processor and spans-appsec-sampling-processor) cannot be renamed or removed.

        :param filter_id: The ID of the retention filter.
        :type filter_id: str
        :param body: The updated definition of the retention filter.
        :type body: RetentionFilterUpdateRequest
        :rtype: RetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["filter_id"] = filter_id

        kwargs["body"] = body

        return self._update_apm_retention_filter_endpoint.call_with_http_info(**kwargs)
