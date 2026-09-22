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
from datadog_api_client.v2.model.terraform_backend_list_response import TerraformBackendListResponse
from datadog_api_client.v2.model.terraform_backend_response import TerraformBackendResponse
from datadog_api_client.v2.model.terraform_backend_create_request import TerraformBackendCreateRequest
from datadog_api_client.v2.model.terraform_backend_update_request import TerraformBackendUpdateRequest


class TerraformStateFilesApi:
    """
    Configure synchronization of Terraform state files from S3 buckets and inspect synchronization status.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_terraform_backend_sync_config_endpoint = _Endpoint(
            settings={
                "response_type": (TerraformBackendResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/iac-api/terraform/backends",
                "operation_id": "create_terraform_backend_sync_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TerraformBackendCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_terraform_backend_sync_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/iac-api/terraform/backends/{id}",
                "operation_id": "delete_terraform_backend_sync_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._list_terraform_backend_sync_configs_endpoint = _Endpoint(
            settings={
                "response_type": (TerraformBackendListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/iac-api/terraform/backends",
                "operation_id": "list_terraform_backend_sync_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_terraform_backend_sync_config_endpoint = _Endpoint(
            settings={
                "response_type": (TerraformBackendResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/iac-api/terraform/backends/{id}",
                "operation_id": "update_terraform_backend_sync_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TerraformBackendUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_terraform_backend_sync_config(
        self,
        body: TerraformBackendCreateRequest,
    ) -> TerraformBackendResponse:
        """Create a Terraform backend sync configuration.

        Create a Terraform backend sync configuration for an AWS account, region, and set of S3 buckets.

        :type body: TerraformBackendCreateRequest
        :rtype: TerraformBackendResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_terraform_backend_sync_config_endpoint.call_with_http_info(**kwargs)

    def delete_terraform_backend_sync_config(
        self,
        id: str,
    ) -> None:
        """Delete a Terraform backend sync configuration.

        Delete a Terraform backend sync configuration and its synchronized state files.

        :param id: Terraform backend sync configuration ID.
        :type id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._delete_terraform_backend_sync_config_endpoint.call_with_http_info(**kwargs)

    def list_terraform_backend_sync_configs(
        self,
        *,
        account_id: Union[str, UnsetType] = unset,
    ) -> TerraformBackendListResponse:
        """List Terraform backend sync configurations.

        List Terraform backend sync configurations, optionally filtered by AWS account ID.

        :param account_id: AWS account ID used to filter configurations. Omit to list all configurations for the organization.
        :type account_id: str, optional
        :rtype: TerraformBackendListResponse
        """
        kwargs: Dict[str, Any] = {}
        if account_id is not unset:
            kwargs["account_id"] = account_id

        return self._list_terraform_backend_sync_configs_endpoint.call_with_http_info(**kwargs)

    def update_terraform_backend_sync_config(
        self,
        id: str,
        body: TerraformBackendUpdateRequest,
    ) -> TerraformBackendResponse:
        """Update a Terraform backend sync configuration.

        Replace the complete set of buckets in a Terraform backend sync configuration. The account and region cannot be changed. The resource ID in the request body must match the path ID; a mismatch returns 409 Conflict.

        :param id: Terraform backend sync configuration ID.
        :type id: str
        :type body: TerraformBackendUpdateRequest
        :rtype: TerraformBackendResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        kwargs["body"] = body

        return self._update_terraform_backend_sync_config_endpoint.call_with_http_info(**kwargs)
