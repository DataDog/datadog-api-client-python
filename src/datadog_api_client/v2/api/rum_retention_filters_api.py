# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_retention_filters_order_response import RumRetentionFiltersOrderResponse
from datadog_api_client.v2.model.rum_retention_filters_order_request import RumRetentionFiltersOrderRequest
from datadog_api_client.v2.model.rum_retention_filters_response import RumRetentionFiltersResponse
from datadog_api_client.v2.model.rum_retention_filter_response import RumRetentionFilterResponse
from datadog_api_client.v2.model.rum_retention_filter_create_request import RumRetentionFilterCreateRequest
from datadog_api_client.v2.model.rum_retention_filter_update_request import RumRetentionFilterUpdateRequest


class RumRetentionFiltersApi:
    """
    Manage retention filters through `Manage Applications <https://app.datadoghq.com/rum/list>`_ of RUM for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters",
                "operation_id": "create_retention_filter",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumRetentionFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}",
                "operation_id": "delete_retention_filter",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "rf_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rf_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}",
                "operation_id": "get_retention_filter",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "rf_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rf_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters",
                "operation_id": "list_retention_filters",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._order_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionFiltersOrderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/relationships/retention_filters",
                "operation_id": "order_retention_filters",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumRetentionFiltersOrderRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/{rf_id}",
                "operation_id": "update_retention_filter",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "rf_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rf_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumRetentionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_retention_filter(
        self,
        app_id: str,
        body: RumRetentionFilterCreateRequest,
    ) -> RumRetentionFilterResponse:
        """Create a RUM retention filter.

        Create a RUM retention filter for a RUM application.
        Returns RUM retention filter objects from the request body when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param body: The definition of the new RUM retention filter.
        :type body: RumRetentionFilterCreateRequest
        :rtype: RumRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._create_retention_filter_endpoint.call_with_http_info(**kwargs)

    def delete_retention_filter(
        self,
        app_id: str,
        rf_id: str,
    ) -> None:
        """Delete a RUM retention filter.

        Delete a RUM retention filter for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Retention filter ID.
        :type rf_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        return self._delete_retention_filter_endpoint.call_with_http_info(**kwargs)

    def get_retention_filter(
        self,
        app_id: str,
        rf_id: str,
    ) -> RumRetentionFilterResponse:
        """Get a RUM retention filter.

        Get a RUM retention filter for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Retention filter ID.
        :type rf_id: str
        :rtype: RumRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        return self._get_retention_filter_endpoint.call_with_http_info(**kwargs)

    def list_retention_filters(
        self,
        app_id: str,
    ) -> RumRetentionFiltersResponse:
        """Get all RUM retention filters.

        Get the list of RUM retention filters for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :rtype: RumRetentionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._list_retention_filters_endpoint.call_with_http_info(**kwargs)

    def order_retention_filters(
        self,
        app_id: str,
        body: RumRetentionFiltersOrderRequest,
    ) -> RumRetentionFiltersOrderResponse:
        """Order RUM retention filters.

        Order RUM retention filters for a RUM application.
        Returns RUM retention filter objects without attributes from the request body when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param body: New definition of the RUM retention filter.
        :type body: RumRetentionFiltersOrderRequest
        :rtype: RumRetentionFiltersOrderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._order_retention_filters_endpoint.call_with_http_info(**kwargs)

    def update_retention_filter(
        self,
        app_id: str,
        rf_id: str,
        body: RumRetentionFilterUpdateRequest,
    ) -> RumRetentionFilterResponse:
        """Update a RUM retention filter.

        Update a RUM retention filter for a RUM application.
        Returns RUM retention filter objects from the request body when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Retention filter ID.
        :type rf_id: str
        :param body: New definition of the RUM retention filter.
        :type body: RumRetentionFilterUpdateRequest
        :rtype: RumRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        kwargs["body"] = body

        return self._update_retention_filter_endpoint.call_with_http_info(**kwargs)
