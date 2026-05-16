# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_permanent_retention_filters_response import RumPermanentRetentionFiltersResponse
from datadog_api_client.v2.model.rum_permanent_retention_filter_response import RumPermanentRetentionFilterResponse
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_request import (
    RumPermanentRetentionFilterUpdateRequest,
)


class RumRetentionFiltersPermanentApi:
    """
    Manage permanent retention filters through `Manage Applications <https://app.datadoghq.com/rum/list>`_ in RUM for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_permanent_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RumPermanentRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/permanent_retention_filters/{rf_id}",
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

        self._list_permanent_retention_filters_endpoint = _Endpoint(
            settings={
                "response_type": (RumPermanentRetentionFiltersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/permanent_retention_filters",
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

        self._update_permanent_retention_filter_endpoint = _Endpoint(
            settings={
                "response_type": (RumPermanentRetentionFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/applications/{app_id}/permanent_retention_filters/{rf_id}",
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
                "rf_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rf_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumPermanentRetentionFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_permanent_retention_filter(
        self,
        app_id: str,
        rf_id: str,
    ) -> RumPermanentRetentionFilterResponse:
        """Get a permanent retention filter.

        Get a single permanent retention filter for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Permanent retention filter ID.
        :type rf_id: str
        :rtype: RumPermanentRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        return self._get_permanent_retention_filter_endpoint.call_with_http_info(**kwargs)

    def list_permanent_retention_filters(
        self,
        app_id: str,
    ) -> RumPermanentRetentionFiltersResponse:
        """Get all permanent retention filters.

        Get the list of permanent retention filters for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: str
        :rtype: RumPermanentRetentionFiltersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._list_permanent_retention_filters_endpoint.call_with_http_info(**kwargs)

    def update_permanent_retention_filter(
        self,
        app_id: str,
        rf_id: str,
        body: RumPermanentRetentionFilterUpdateRequest,
    ) -> RumPermanentRetentionFilterResponse:
        """Update a permanent retention filter.

        Update the cross-product sample rates of a permanent retention filter for a RUM application.
        Only ``cross_product_sampling.trace_sample_rate`` can be updated,
        and only when the matching flag in ``cross_product_sampling_editability`` is ``true`` on the filter.
        Any other field is read-only and cannot be sent in the payload.
        Returns the updated permanent retention filter when the request is successful.

        :param app_id: RUM application ID.
        :type app_id: str
        :param rf_id: Permanent retention filter ID.
        :type rf_id: str
        :param body: New cross-product sample rates for the permanent retention filter.
        :type body: RumPermanentRetentionFilterUpdateRequest
        :rtype: RumPermanentRetentionFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["rf_id"] = rf_id

        kwargs["body"] = body

        return self._update_permanent_retention_filter_endpoint.call_with_http_info(**kwargs)
