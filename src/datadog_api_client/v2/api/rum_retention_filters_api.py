# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_retention_filters_order_response import RUMRetentionFiltersOrderResponse
from datadog_api_client.v2.model.rum_retention_filters_order_request import RUMRetentionFiltersOrderRequest
from datadog_api_client.v2.model.rum_retention_filters_response import RUMRetentionFiltersResponse
from datadog_api_client.v2.model.rum_retention_filter_response import RUMRetentionFilterResponse
from datadog_api_client.v2.model.rum_retention_filter_create_request import RUMRetentionFilterCreateRequest
from datadog_api_client.v2.model.rum_exclusion_filters_response import RUMExclusionFiltersResponse
from datadog_api_client.v2.model.rum_exclusion_filter_response import RUMExclusionFilterResponse
from datadog_api_client.v2.model.rum_exclusion_filter_create_request import RUMExclusionFilterCreateRequest
from datadog_api_client.v2.model.rum_exclusion_filter_update_request import RUMExclusionFilterUpdateRequest
from datadog_api_client.v2.model.rum_permanent_retention_filters_response import RUMPermanentRetentionFiltersResponse
from datadog_api_client.v2.model.rum_permanent_retention_filter_response import RUMPermanentRetentionFilterResponse
from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RUMPermanentRetentionFilterID
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_request import (
    RUMPermanentRetentionFilterUpdateRequest,
)
from datadog_api_client.v2.model.rum_retention_filter_update_request import RUMRetentionFilterUpdateRequest


class RUMRetentionFiltersApi:
    """
    Manage retention filters through `Manage Applications <https://app.datadoghq.com/rum/list>`_ of RUM for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/exclusion",
                "operation_id": "create_exclusion_filter",
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
                    "openapi_types": (RUMExclusionFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                    "openapi_types": (RUMRetentionFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/exclusion/{ef_id}",
                "operation_id": "delete_exclusion_filter",
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
                "ef_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ef_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._get_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/exclusion/{ef_id}",
                "operation_id": "get_exclusion_filter",
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
                "ef_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ef_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_permanent_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMPermanentRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/permanent/{permanent_rf_id}",
                "operation_id": "get_permanent_retention_filter",
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
                "permanent_rf_id": {
                    "required": True,
                    "openapi_types": (RUMPermanentRetentionFilterID,),
                    "attribute": "permanent_rf_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._list_exclusion_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RUMExclusionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/exclusion",
                "operation_id": "list_exclusion_filters",
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

        self._list_permanent_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RUMPermanentRetentionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/permanent",
                "operation_id": "list_permanent_retention_filters",
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

        self._list_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RUMRetentionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "response_type": (RUMRetentionFiltersOrderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                    "openapi_types": (RUMRetentionFiltersOrderRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_exclusion_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMExclusionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/exclusion/{ef_id}",
                "operation_id": "update_exclusion_filter",
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
                "ef_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "ef_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RUMExclusionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_permanent_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMPermanentRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/retention_filters/permanent/{permanent_rf_id}",
                "operation_id": "update_permanent_retention_filter",
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
                "permanent_rf_id": {
                    "required": True,
                    "openapi_types": (RUMPermanentRetentionFilterID,),
                    "attribute": "permanent_rf_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RUMPermanentRetentionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RUMRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                    "openapi_types": (RUMRetentionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_exclusion_filter(
        self,
        app_id: str,
        body: RUMExclusionFilterCreateRequest,
    ) -> RUMExclusionFilterResponse:
        """Create a RUM exclusion filter.

        Create an exclusion filter for a RUM application.
        Returns the created exclusion filter when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param body: The definition of the new RUM exclusion filter.
        :type body: RUMExclusionFilterCreateRequest
        :rtype: RUMExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._create_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def create_retention_filter(
        self,
        app_id: str,
        body: RUMRetentionFilterCreateRequest,
    ) -> RUMRetentionFilterResponse:
        """Create a RUM retention filter.

        Create a RUM retention filter for a RUM application.
        Returns RUM retention filter objects from the request body when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param body: The definition of the new RUM retention filter.
        :type body: RUMRetentionFilterCreateRequest
        :rtype: RUMRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._create_retention_filter_endpoint.call_with_http_info(**kwargs)

    def delete_exclusion_filter(
        self,
        app_id: str,
        ef_id: str,
    ) -> None:
        """Delete a RUM exclusion filter.

        Delete an exclusion filter for a RUM application.
        The built-in Error Tracking exclusion filter ( ``error_tracking_exclusion_filter`` ) cannot be deleted;
        attempting to do so returns a ``405 Method Not Allowed`` response.

        :param app_id: RUM application ID.
        :type app_id: str
        :param ef_id: Exclusion filter ID.
        :type ef_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["ef_id"] = ef_id

        return self._delete_exclusion_filter_endpoint.call_with_http_info(**kwargs)

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

    def get_exclusion_filter(
        self,
        app_id: str,
        ef_id: str,
    ) -> RUMExclusionFilterResponse:
        """Get a RUM exclusion filter.

        Get a single exclusion filter for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :param ef_id: Exclusion filter ID.
        :type ef_id: str
        :rtype: RUMExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["ef_id"] = ef_id

        return self._get_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def get_permanent_retention_filter(
        self,
        app_id: str,
        permanent_rf_id: RUMPermanentRetentionFilterID,
    ) -> RUMPermanentRetentionFilterResponse:
        """Get a permanent RUM retention filter.

        Get a permanent RUM retention filter for a RUM application by its identifier.

        :param app_id: RUM application ID.
        :type app_id: str
        :param permanent_rf_id: The identifier of the permanent RUM retention filter.
        :type permanent_rf_id: RUMPermanentRetentionFilterID
        :rtype: RUMPermanentRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["permanent_rf_id"] = permanent_rf_id

        return self._get_permanent_retention_filter_endpoint.call_with_http_info(**kwargs)

    def get_retention_filter(
        self,
        app_id: str,
        rf_id: str,
    ) -> RUMRetentionFilterResponse:
        """Get a RUM retention filter.

        Get a RUM retention filter for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Retention filter ID.
        :type rf_id: str
        :rtype: RUMRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        return self._get_retention_filter_endpoint.call_with_http_info(**kwargs)

    def list_exclusion_filters(
        self,
        app_id: str,
    ) -> RUMExclusionFiltersResponse:
        """Get all RUM exclusion filters.

        Get the list of exclusion filters for a RUM application.
        The built-in Error Tracking exclusion filter ( ``error_tracking_exclusion_filter`` ) is always returned first.

        :param app_id: RUM application ID.
        :type app_id: str
        :rtype: RUMExclusionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._list_exclusion_filters_endpoint.call_with_http_info(**kwargs)

    def list_permanent_retention_filters(
        self,
        app_id: str,
    ) -> RUMPermanentRetentionFiltersResponse:
        """Get all permanent RUM retention filters.

        Get the list of permanent RUM retention filters for a RUM application.
        Permanent retention filters are predefined filters that cannot be created or deleted.
        For each filter, the ``editability`` block indicates which cross-product fields can be updated.

        :param app_id: RUM application ID.
        :type app_id: str
        :rtype: RUMPermanentRetentionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._list_permanent_retention_filters_endpoint.call_with_http_info(**kwargs)

    def list_retention_filters(
        self,
        app_id: str,
    ) -> RUMRetentionFiltersResponse:
        """Get all RUM retention filters.

        Get the list of RUM retention filters for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :rtype: RUMRetentionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._list_retention_filters_endpoint.call_with_http_info(**kwargs)

    def order_retention_filters(
        self,
        app_id: str,
        body: RUMRetentionFiltersOrderRequest,
    ) -> RUMRetentionFiltersOrderResponse:
        """Order RUM retention filters.

        Order RUM retention filters for a RUM application.
        Returns RUM retention filter objects without attributes from the request body when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param body: New definition of the RUM retention filter.
        :type body: RUMRetentionFiltersOrderRequest
        :rtype: RUMRetentionFiltersOrderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._order_retention_filters_endpoint.call_with_http_info(**kwargs)

    def update_exclusion_filter(
        self,
        app_id: str,
        ef_id: str,
        body: RUMExclusionFilterUpdateRequest,
    ) -> RUMExclusionFilterResponse:
        """Update a RUM exclusion filter.

        Update an exclusion filter for a RUM application.
        For the built-in Error Tracking exclusion filter ( ``error_tracking_exclusion_filter`` ), only ``enabled`` can be
        updated; ``name`` , ``event_type`` , and ``query`` must be omitted.
        Returns the updated exclusion filter when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param ef_id: Exclusion filter ID.
        :type ef_id: str
        :param body: New definition of the RUM exclusion filter.
        :type body: RUMExclusionFilterUpdateRequest
        :rtype: RUMExclusionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["ef_id"] = ef_id

        kwargs["body"] = body

        return self._update_exclusion_filter_endpoint.call_with_http_info(**kwargs)

    def update_permanent_retention_filter(
        self,
        app_id: str,
        permanent_rf_id: RUMPermanentRetentionFilterID,
        body: RUMPermanentRetentionFilterUpdateRequest,
    ) -> RUMPermanentRetentionFilterResponse:
        """Update a permanent RUM retention filter.

        Update the cross-product sampling configuration of a permanent RUM retention filter for a RUM application.
        Only fields marked as editable in the ``editability`` block of the filter can be updated.
        Updating a non-editable field returns a ``400`` response.

        :param app_id: RUM application ID.
        :type app_id: str
        :param permanent_rf_id: The identifier of the permanent RUM retention filter.
        :type permanent_rf_id: RUMPermanentRetentionFilterID
        :param body: New configuration of the permanent RUM retention filter.
        :type body: RUMPermanentRetentionFilterUpdateRequest
        :rtype: RUMPermanentRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["permanent_rf_id"] = permanent_rf_id

        kwargs["body"] = body

        return self._update_permanent_retention_filter_endpoint.call_with_http_info(**kwargs)

    def update_retention_filter(
        self,
        app_id: str,
        rf_id: str,
        body: RUMRetentionFilterUpdateRequest,
    ) -> RUMRetentionFilterResponse:
        """Update a RUM retention filter.

        Update a RUM retention filter for a RUM application.
        Returns RUM retention filter objects from the request body when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Retention filter ID.
        :type rf_id: str
        :param body: New definition of the RUM retention filter.
        :type body: RUMRetentionFilterUpdateRequest
        :rtype: RUMRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        kwargs["body"] = body

        return self._update_retention_filter_endpoint.call_with_http_info(**kwargs)
