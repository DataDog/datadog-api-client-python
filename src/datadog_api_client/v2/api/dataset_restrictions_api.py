# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.dataset_restrictions_list_response import DatasetRestrictionsListResponse
from datadog_api_client.v2.model.dataset_restriction_response import DatasetRestrictionResponse
from datadog_api_client.v2.model.dataset_restriction_update_request import DatasetRestrictionUpdateRequest


class DatasetRestrictionsApi:
    """
    Configure dataset-level access restrictions per Datadog product type. Dataset restrictions
    control whether data is visible by default or hidden until explicitly granted, and how
    ownership-based access is determined.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_dataset_restrictions_endpoint = _Endpoint(
            settings={
                "response_type": (DatasetRestrictionsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dataset_restrictions",
                "operation_id": "list_dataset_restrictions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_dataset_restriction_endpoint = _Endpoint(
            settings={
                "response_type": (DatasetRestrictionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dataset_restrictions/{product_type}",
                "operation_id": "update_dataset_restriction",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "product_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "product_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DatasetRestrictionUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def list_dataset_restrictions(
        self,
    ) -> DatasetRestrictionsListResponse:
        """List dataset restrictions.

        Retrieve all dataset restriction configurations for the organization.
        Returns one restriction object per configured product type (for example, RUM, APM, or Logs),
        including the current restriction mode, ownership mode, and any unrestricted principals.
        Requires the ``user_access_read`` permission.

        :rtype: DatasetRestrictionsListResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_dataset_restrictions_endpoint.call_with_http_info(**kwargs)

    def update_dataset_restriction(
        self,
        product_type: str,
        body: DatasetRestrictionUpdateRequest,
    ) -> DatasetRestrictionResponse:
        """Update a dataset restriction.

        Update the dataset restriction configuration for a specific product type.
        Sets the restriction mode, optional ownership mode, and the list of principals
        that are exempt from restrictions. Requires the ``user_access_manage`` permission.
        Changes are audited and take effect immediately.

        :param product_type: The Datadog product type to configure restrictions for (for example, ``rum`` , ``apm`` , or ``logs`` ).
        :type product_type: str
        :type body: DatasetRestrictionUpdateRequest
        :rtype: DatasetRestrictionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["product_type"] = product_type

        kwargs["body"] = body

        return self._update_dataset_restriction_endpoint.call_with_http_info(**kwargs)
