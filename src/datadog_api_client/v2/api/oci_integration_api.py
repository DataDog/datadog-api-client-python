# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.tenancy_config_list import TenancyConfigList
from datadog_api_client.v2.model.tenancy_config import TenancyConfig
from datadog_api_client.v2.model.create_tenancy_config import CreateTenancyConfig
from datadog_api_client.v2.model.update_tenancy_config import UpdateTenancyConfig


class OCIIntegrationApi:
    """
    Configure your Datadog-OCI integration directly through the Datadog API.
    For more information, see the `OCI integration page <https://docs.datadoghq.com/integrations/oracle_cloud_infrastructure/>`_.
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
                    "openapi_types": (CreateTenancyConfig,),
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
                    "openapi_types": (UpdateTenancyConfig,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_tenancy_config(
        self,
        body: CreateTenancyConfig,
    ) -> TenancyConfig:
        """Create tenancy config.

        Create a new tenancy config.

        :type body: CreateTenancyConfig
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

        Delete an existing tenancy config.

        :param tenancy_ocid: Unique tenancy OCID of the OCI integration config.
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

        Get a single tenancy config object.

        :param tenancy_ocid: Unique tenancy OCID of the OCI integration config.
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

        List all tenancy integrations.

        :rtype: TenancyConfigList
        """
        kwargs: Dict[str, Any] = {}
        return self._get_tenancy_configs_endpoint.call_with_http_info(**kwargs)

    def update_tenancy_config(
        self,
        tenancy_ocid: str,
        body: UpdateTenancyConfig,
    ) -> TenancyConfig:
        """Update tenancy config.

        Update an existing tenancy config.

        :param tenancy_ocid: Unique tenancy OCID of the OCI integration config.
        :type tenancy_ocid: str
        :type body: UpdateTenancyConfig
        :rtype: TenancyConfig
        """
        kwargs: Dict[str, Any] = {}
        kwargs["tenancy_ocid"] = tenancy_ocid

        kwargs["body"] = body

        return self._update_tenancy_config_endpoint.call_with_http_info(**kwargs)
