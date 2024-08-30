# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_accounts_response import AWSAccountsResponse
from datadog_api_client.v2.model.aws_account_response import AWSAccountResponse
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_patch_request import AWSAccountPatchRequest


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

        self._delete_aws_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/aws/accounts/{aws_account_id}",
                "operation_id": "delete_aws_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "aws_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aws_account_id",
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
                "endpoint_path": "/api/v2/integration/aws/accounts/{aws_account_id}",
                "operation_id": "get_aws_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "aws_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aws_account_id",
                    "location": "path",
                },
            },
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
                "endpoint_path": "/api/v2/integration/aws/accounts/{aws_account_id}",
                "operation_id": "update_aws_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "aws_account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aws_account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AWSAccountPatchRequest,),
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
        """AWS Integration - Create account config.

        Create a new AWS Account Integration Config

        :type body: AWSAccountCreateRequest
        :rtype: AWSAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_account_endpoint.call_with_http_info(**kwargs)

    def delete_aws_account(
        self,
        aws_account_id: str,
    ) -> None:
        """AWS Integration - Delete account config.

        Delete an AWS Account Integration Config

        :param aws_account_id: The ID of the AWS Account Integration Config
        :type aws_account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aws_account_id"] = aws_account_id

        return self._delete_aws_account_endpoint.call_with_http_info(**kwargs)

    def get_aws_account(
        self,
        aws_account_id: str,
    ) -> AWSAccountResponse:
        """AWS Integration - Get account config.

        Get an AWS Account Integration Config

        :param aws_account_id: The ID of the AWS Account Integration Config
        :type aws_account_id: str
        :rtype: AWSAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aws_account_id"] = aws_account_id

        return self._get_aws_account_endpoint.call_with_http_info(**kwargs)

    def list_aws_accounts(
        self,
    ) -> AWSAccountsResponse:
        """AWS Integration - Get all account configs.

        Get all AWS Account Integration Configs

        :rtype: AWSAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_accounts_endpoint.call_with_http_info(**kwargs)

    def update_aws_account(
        self,
        aws_account_id: str,
        body: AWSAccountPatchRequest,
    ) -> AWSAccountResponse:
        """AWS Integration - Patch account config.

        Update an AWS Account Integration Config

        :param aws_account_id: The ID of the AWS Account Integration Config
        :type aws_account_id: str
        :type body: AWSAccountPatchRequest
        :rtype: AWSAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aws_account_id"] = aws_account_id

        kwargs["body"] = body

        return self._update_aws_account_endpoint.call_with_http_info(**kwargs)
