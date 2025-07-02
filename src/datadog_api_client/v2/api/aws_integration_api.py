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
from datadog_api_client.v2.model.aws_accounts_response import AWSAccountsResponse
from datadog_api_client.v2.model.aws_account_response import AWSAccountResponse
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_update_request import AWSAccountUpdateRequest
from datadog_api_client.v2.model.aws_namespaces_response import AWSNamespacesResponse
from datadog_api_client.v2.model.aws_new_external_id_response import AWSNewExternalIDResponse
from datadog_api_client.v2.model.aws_integration_iam_permissions_response import AWSIntegrationIamPermissionsResponse


class AWSIntegrationApi:
    """
    Configure your Datadog-AWS integration directly through the Datadog API.
    For more information, see the `AWS integration page <https://docs.datadoghq.com/integrations/amazon_web_services>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/accounts",
                "operation_id": "create_aws_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_new_aws_external_id_endpoint = _Endpoint(
            settings={
                "response_type": (AWSNewExternalIDResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/generate_new_external_id",
                "operation_id": "create_new_aws_external_id",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._delete_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/accounts/{aws_account_config_id}",
                "operation_id": "delete_aws_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "aws_account_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aws_account_config_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/accounts/{aws_account_config_id}",
                "operation_id": "get_aws_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "aws_account_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aws_account_config_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_aws_integration_iam_permissions_endpoint = _Endpoint(
            settings={
                "response_type": (AWSIntegrationIamPermissionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/iam_permissions",
                "operation_id": "get_aws_integration_iam_permissions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/accounts",
                "operation_id": "list_aws_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "aws_account_id": {
                    "openapi_types": (str,),
                    "attribute": "aws_account_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_namespaces_endpoint = _Endpoint(
            settings={
                "response_type": (AWSNamespacesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/available_namespaces",
                "operation_id": "list_aws_namespaces",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": (AWSAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/accounts/{aws_account_config_id}",
                "operation_id": "update_aws_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "aws_account_config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aws_account_config_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_aws_account(
        self,
        body: AWSAccountCreateRequest,
    ) -> AWSAccountResponse:
        """Create an AWS integration.

        Create a new AWS Account Integration Config.

        :type body: AWSAccountCreateRequest
        :rtype: AWSAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_account_endpoint.call_with_http_info(**kwargs)

    def create_new_aws_external_id(
        self,
    ) -> AWSNewExternalIDResponse:
        """Generate a new external ID.

        Generate a new external ID for AWS role-based authentication.

        :rtype: AWSNewExternalIDResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._create_new_aws_external_id_endpoint.call_with_http_info(**kwargs)

    def delete_aws_account(
        self,
        aws_account_config_id: str,
    ) -> None:
        """Delete an AWS integration.

        Delete an AWS Account Integration Config by config ID.

        :param aws_account_config_id: Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the
            `List all AWS integrations <https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations>`_ endpoint and query by AWS Account ID.
        :type aws_account_config_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aws_account_config_id"] = aws_account_config_id

        return self._delete_aws_account_endpoint.call_with_http_info(**kwargs)

    def get_aws_account(
        self,
        aws_account_config_id: str,
    ) -> AWSAccountResponse:
        """Get an AWS integration by config ID.

        Get an AWS Account Integration Config by config ID.

        :param aws_account_config_id: Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the
            `List all AWS integrations <https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations>`_ endpoint and query by AWS Account ID.
        :type aws_account_config_id: str
        :rtype: AWSAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aws_account_config_id"] = aws_account_config_id

        return self._get_aws_account_endpoint.call_with_http_info(**kwargs)

    def get_aws_integration_iam_permissions(
        self,
    ) -> AWSIntegrationIamPermissionsResponse:
        """Get AWS integration IAM permissions.

        Get all AWS IAM permissions required for the AWS integration.

        :rtype: AWSIntegrationIamPermissionsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_aws_integration_iam_permissions_endpoint.call_with_http_info(**kwargs)

    def list_aws_accounts(
        self,
        *,
        aws_account_id: Union[str, UnsetType] = unset,
    ) -> AWSAccountsResponse:
        """List all AWS integrations.

        Get a list of AWS Account Integration Configs.

        :param aws_account_id: Optional query parameter to filter accounts by AWS Account ID. If not provided, all accounts are returned.
        :type aws_account_id: str, optional
        :rtype: AWSAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        if aws_account_id is not unset:
            kwargs["aws_account_id"] = aws_account_id

        return self._list_aws_accounts_endpoint.call_with_http_info(**kwargs)

    def list_aws_namespaces(
        self,
    ) -> AWSNamespacesResponse:
        """List available namespaces.

        Get a list of available AWS CloudWatch namespaces that can send metrics to Datadog.

        :rtype: AWSNamespacesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_namespaces_endpoint.call_with_http_info(**kwargs)

    def update_aws_account(
        self,
        aws_account_config_id: str,
        body: AWSAccountUpdateRequest,
    ) -> AWSAccountResponse:
        """Update an AWS integration.

        Update an AWS Account Integration Config by config ID.

        :param aws_account_config_id: Unique Datadog ID of the AWS Account Integration Config. To get the config ID for an account, use the
            `List all AWS integrations <https://docs.datadoghq.com/api/latest/aws-integration/#list-all-aws-integrations>`_ endpoint and query by AWS Account ID.
        :type aws_account_config_id: str
        :type body: AWSAccountUpdateRequest
        :rtype: AWSAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aws_account_config_id"] = aws_account_config_id

        kwargs["body"] = body

        return self._update_aws_account_endpoint.call_with_http_info(**kwargs)
