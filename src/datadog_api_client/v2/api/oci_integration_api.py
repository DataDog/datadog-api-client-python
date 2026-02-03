# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.tenancy_products_list import TenancyProductsList
from datadog_api_client.v2.model.tenancy_config_list import TenancyConfigList
from datadog_api_client.v2.model.tenancy_config import TenancyConfig
from datadog_api_client.v2.model.create_tenancy_config_request import CreateTenancyConfigRequest
from datadog_api_client.v2.model.update_tenancy_config_request import UpdateTenancyConfigRequest


class OCIIntegrationApi:
    """
    Auto-generated tag OCI Integration
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_tenancy_config_endpoint = _Endpoint(
            settings={
                "response_type": (TenancyConfig,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/oci/tenancies",
                "operation_id": "create_tenancy_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateTenancyConfigRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_tenancy_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/oci/tenancies/{tenancy_ocid}",
                "operation_id": "delete_tenancy_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "tenancy_ocid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "tenancy_ocid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_tenancy_config_endpoint = _Endpoint(
            settings={
                "response_type": (TenancyConfig,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/oci/tenancies/{tenancy_ocid}",
                "operation_id": "get_tenancy_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "tenancy_ocid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "tenancy_ocid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_tenancy_configs_endpoint = _Endpoint(
            settings={
                "response_type": (TenancyConfigList,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/oci/tenancies",
                "operation_id": "get_tenancy_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tenancy_products_endpoint = _Endpoint(
            settings={
                "response_type": (TenancyProductsList,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/oci/products",
                "operation_id": "list_tenancy_products",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "product_keys": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "productKeys",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_tenancy_config_endpoint = _Endpoint(
            settings={
                "response_type": (TenancyConfig,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/oci/tenancies/{tenancy_ocid}",
                "operation_id": "update_tenancy_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "tenancy_ocid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "tenancy_ocid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateTenancyConfigRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_tenancy_config(
        self,
        body: CreateTenancyConfigRequest,
    ) -> TenancyConfig:
        """Create tenancy config.

        Create a new tenancy config to establish monitoring and data collection from your OCI environment. Requires OCI authentication credentials and tenancy details. Warning: Datadog recommends interacting with this endpoint only through the Datadog web UI to ensure all necessary OCI resources have been created and configured properly.

        :type body: CreateTenancyConfigRequest
        :rtype: TenancyConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_tenancy_config_endpoint.call_with_http_info(**kwargs)

    def delete_tenancy_config(
        self,
        tenancy_ocid: str,
    ) -> None:
        """Delete tenancy config.

        Delete an existing tenancy config. This will stop all data collection from the specified OCI tenancy and remove the stored configuration. This operation cannot be undone.

        :param tenancy_ocid: The OCID of the tenancy config to delete.
        :type tenancy_ocid: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["tenancy_ocid"] = tenancy_ocid

        return self._delete_tenancy_config_endpoint.call_with_http_info(**kwargs)

    def get_tenancy_config(
        self,
        tenancy_ocid: str,
    ) -> TenancyConfig:
        """Get tenancy config.

        Get a single tenancy config object by its OCID. Returns detailed configuration including authentication credentials, enabled services, region settings, and collection preferences.

        :param tenancy_ocid: The OCID of the tenancy config to retrieve.
        :type tenancy_ocid: str
        :rtype: TenancyConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["tenancy_ocid"] = tenancy_ocid

        return self._get_tenancy_config_endpoint.call_with_http_info(**kwargs)

    def get_tenancy_configs(
        self,
    ) -> TenancyConfigList:
        """Get tenancy configs.

        Get a list of all configured OCI tenancy integrations. Returns basic information about each tenancy including authentication credentials, region settings, and collection preferences for metrics, logs, and resources.

        :rtype: TenancyConfigList
        """
        kwargs: Dict[str, Any] = {}
        return self._get_tenancy_configs_endpoint.call_with_http_info(**kwargs)

    def list_tenancy_products(
        self,
        product_keys: str,
    ) -> TenancyProductsList:
        """List tenancy products.

        Lists the products for a given tenancy. Returns the enabled/disabled status of Datadog products (such as Cloud Security Posture Management) for specific OCI tenancies.

        :param product_keys: Comma-separated list of product keys to filter by.
        :type product_keys: str
        :rtype: TenancyProductsList
        """
        kwargs: Dict[str, Any] = {}
        kwargs["product_keys"] = product_keys

        return self._list_tenancy_products_endpoint.call_with_http_info(**kwargs)

    def update_tenancy_config(
        self,
        tenancy_ocid: str,
        body: UpdateTenancyConfigRequest,
    ) -> TenancyConfig:
        """Update tenancy config.

        Update an existing tenancy config. You can modify authentication credentials, enable/disable collection types, update service filters, and change region settings. Warning: We recommend using the Datadog web UI to avoid unintended update effects.

        :param tenancy_ocid: The OCID of the tenancy config to update.
        :type tenancy_ocid: str
        :type body: UpdateTenancyConfigRequest
        :rtype: TenancyConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["tenancy_ocid"] = tenancy_ocid

        kwargs["body"] = body

        return self._update_tenancy_config_endpoint.call_with_http_info(**kwargs)
