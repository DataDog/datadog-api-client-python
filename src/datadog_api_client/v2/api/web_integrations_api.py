# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.web_integration_accounts_response import WebIntegrationAccountsResponse
from datadog_api_client.v2.model.web_integration_account_response import WebIntegrationAccountResponse
from datadog_api_client.v2.model.web_integration_account_create_request import WebIntegrationAccountCreateRequest
from datadog_api_client.v2.model.web_integration_account_schema_response import WebIntegrationAccountSchemaResponse
from datadog_api_client.v2.model.web_integration_account_update_request import WebIntegrationAccountUpdateRequest


class WebIntegrationsApi:
    """
    Configure and manage third-party web integrations with Datadog. This API provides a unified
    interface for managing integration accounts across various external services.

    Each integration has its own unique schema that defines the required settings and secrets.
    Before creating or updating an account, use the schema endpoint to retrieve the specific
    requirements, field types, validation rules, and available configuration options for your
    integration.

    Supported Integrations:

    * twilio
    * snowflake-web
    * databricks
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_web_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (WebIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/web-integrations/{integration_name}/accounts",
                "operation_id": "create_web_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "integration_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WebIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_web_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/web-integrations/{integration_name}/accounts/{account_id}",
                "operation_id": "delete_web_integration_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "integration_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_name",
                    "location": "path",
                },
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_web_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (WebIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/web-integrations/{integration_name}/accounts/{account_id}",
                "operation_id": "get_web_integration_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_name",
                    "location": "path",
                },
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_web_integration_account_schema_endpoint = _Endpoint(
            settings={
                "response_type": (WebIntegrationAccountSchemaResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/web-integrations/{integration_name}/accounts/schema",
                "operation_id": "get_web_integration_account_schema",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_web_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (WebIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/web-integrations/{integration_name}/accounts",
                "operation_id": "list_web_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_web_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (WebIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/web-integrations/{integration_name}/accounts/{account_id}",
                "operation_id": "update_web_integration_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "integration_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "integration_name",
                    "location": "path",
                },
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WebIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_web_integration_account(
        self,
        integration_name: str,
        body: WebIntegrationAccountCreateRequest,
    ) -> WebIntegrationAccountResponse:
        """Create integration account.

        Create a new account for a specific integration. The account configuration must conform
        to the schema defined for the integration, which can be retrieved using the schema endpoint.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :type body: WebIntegrationAccountCreateRequest
        :rtype: WebIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["body"] = body

        return self._create_web_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_web_integration_account(
        self,
        integration_name: str,
        account_id: str,
    ) -> None:
        """Delete integration account.

        Delete a specific account by its ID for a given integration. This will remove the
        account configuration and stop any data collection associated with it.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param account_id: The unique identifier of the account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["account_id"] = account_id

        return self._delete_web_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_web_integration_account(
        self,
        integration_name: str,
        account_id: str,
    ) -> WebIntegrationAccountResponse:
        """Get integration account.

        Retrieve a specific account by its ID for a given integration. The response includes
        the account name and settings, but excludes sensitive secret values.

        Rate limit: 12000 requests per organization every 60 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param account_id: The unique identifier of the account.
        :type account_id: str
        :rtype: WebIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["account_id"] = account_id

        return self._get_web_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_web_integration_account_schema(
        self,
        integration_name: str,
    ) -> WebIntegrationAccountSchemaResponse:
        """Get account schema for an integration.

        Get the JSON schema that defines the structure and validation rules for account configuration
        of a specific integration. This schema describes the required and optional fields for both
        settings and secrets when creating or updating an account.

        Rate limit: 12000 requests per organization every 60 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :rtype: WebIntegrationAccountSchemaResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        return self._get_web_integration_account_schema_endpoint.call_with_http_info(**kwargs)

    def list_web_integration_accounts(
        self,
        integration_name: str,
    ) -> WebIntegrationAccountsResponse:
        """List integration accounts.

        Retrieve all configured accounts for a specific integration within your organization.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :rtype: WebIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        return self._list_web_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_web_integration_account(
        self,
        integration_name: str,
        account_id: str,
        body: WebIntegrationAccountUpdateRequest,
    ) -> WebIntegrationAccountResponse:
        """Update integration account.

        Update an existing account for a specific integration. You can update the name, settings,
        and/or secrets. Only the fields provided in the request will be updated.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param account_id: The unique identifier of the account.
        :type account_id: str
        :type body: WebIntegrationAccountUpdateRequest
        :rtype: WebIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_web_integration_account_endpoint.call_with_http_info(**kwargs)
