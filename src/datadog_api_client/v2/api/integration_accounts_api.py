# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.ams_integration_accounts_response import AmsIntegrationAccountsResponse
from datadog_api_client.v2.model.ams_integration_account_response import AmsIntegrationAccountResponse
from datadog_api_client.v2.model.ams_integration_account_create_request import AmsIntegrationAccountCreateRequest
from datadog_api_client.v2.model.ams_integration_account_schema_response import AmsIntegrationAccountSchemaResponse
from datadog_api_client.v2.model.ams_integration_account_update_request import AmsIntegrationAccountUpdateRequest


class IntegrationAccountsApi:
    """
    Configure and manage third-party integrations with Datadog. This API provides a unified
    interface for managing integration accounts across various external services.

    Each integration has its own unique schema that defines the required settings and secrets.
    Before creating or updating an account, use the schema endpoint to retrieve the specific
    requirements, field types, validation rules, and available configuration options for your
    integration.

    **Note** : This API manages integration account configurations only. It does not support
    Grace Resources, Reference Tables, or Custom Queries CRUD operations. For those features,
    refer to each integration's dedicated documentation.

    Supported Integrations:

    * `Twilio <https://docs.datadoghq.com/integrations/twilio/>`_
    * `Snowflake <https://docs.datadoghq.com/integrations/snowflake-web/>`_
    * `Databricks <https://docs.datadoghq.com/integrations/databricks/>`_
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_ams_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (AmsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_name}/interfaces/{interface_id}/accounts",
                "operation_id": "create_ams_integration_account",
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
                "interface_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "interface_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (AmsIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_ams_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_name}/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "delete_ams_integration_account",
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
                "interface_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "interface_id",
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

        self._get_ams_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (AmsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_name}/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "get_ams_integration_account",
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
                "interface_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "interface_id",
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

        self._get_ams_integration_account_schema_endpoint = _Endpoint(
            settings={
                "response_type": (AmsIntegrationAccountSchemaResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_name}/interfaces/{interface_id}/accounts/schema",
                "operation_id": "get_ams_integration_account_schema",
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
                "interface_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "interface_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_ams_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (AmsIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_name}/interfaces/{interface_id}/accounts",
                "operation_id": "list_ams_integration_accounts",
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
                "interface_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "interface_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_ams_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (AmsIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_name}/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "update_ams_integration_account",
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
                "interface_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "interface_id",
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
                    "openapi_types": (AmsIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_ams_integration_account(
        self,
        integration_name: str,
        interface_id: str,
        body: AmsIntegrationAccountCreateRequest,
    ) -> AmsIntegrationAccountResponse:
        """Create integration account.

        Create a new account for a specific integration. The account configuration must conform
        to the schema defined for the integration, which can be retrieved using the schema endpoint.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param interface_id: The unique identifier of the interface.
        :type interface_id: str
        :type body: AmsIntegrationAccountCreateRequest
        :rtype: AmsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["interface_id"] = interface_id

        kwargs["body"] = body

        return self._create_ams_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_ams_integration_account(
        self,
        integration_name: str,
        interface_id: str,
        account_id: str,
    ) -> None:
        """Delete integration account.

        Delete a specific account by its ID for a given integration. This removes the
        account configuration and stops any data collection associated with it.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param interface_id: The unique identifier of the interface.
        :type interface_id: str
        :param account_id: The unique identifier of the account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._delete_ams_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_ams_integration_account(
        self,
        integration_name: str,
        interface_id: str,
        account_id: str,
    ) -> AmsIntegrationAccountResponse:
        """Get integration account.

        Retrieve a specific account by its ID for a given integration. The response includes
        the account name and settings, but excludes sensitive secret values.

        Rate limit: 12000 requests per organization every 60 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param interface_id: The unique identifier of the interface.
        :type interface_id: str
        :param account_id: The unique identifier of the account.
        :type account_id: str
        :rtype: AmsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._get_ams_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_ams_integration_account_schema(
        self,
        integration_name: str,
        interface_id: str,
    ) -> AmsIntegrationAccountSchemaResponse:
        """Get account schema for an integration.

        Get the JSON schema that defines the structure and validation rules for account configuration
        of a specific integration. This schema describes the required and optional fields for both
        **settings** and **secrets** when creating or updating an account.

        The schema structure varies between integrations, so always retrieve the schema for your
        specific integration before creating or updating accounts.

        Rate limit: 12000 requests per organization every 60 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param interface_id: The unique identifier of the interface.
        :type interface_id: str
        :rtype: AmsIntegrationAccountSchemaResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["interface_id"] = interface_id

        return self._get_ams_integration_account_schema_endpoint.call_with_http_info(**kwargs)

    def list_ams_integration_accounts(
        self,
        integration_name: str,
        interface_id: str,
    ) -> AmsIntegrationAccountsResponse:
        """List integration accounts.

        Retrieve all configured accounts for a specific integration within your organization.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param interface_id: The unique identifier of the interface.
        :type interface_id: str
        :rtype: AmsIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["interface_id"] = interface_id

        return self._list_ams_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_ams_integration_account(
        self,
        integration_name: str,
        interface_id: str,
        account_id: str,
        body: AmsIntegrationAccountUpdateRequest,
    ) -> AmsIntegrationAccountResponse:
        """Update integration account.

        Update an existing account for a specific integration. You can update the name, settings,
        and secrets. Only the fields provided in the request are updated.

        Rate limit: 50 requests per user every 20 seconds.

        :param integration_name: The name of the integration.
        :type integration_name: str
        :param interface_id: The unique identifier of the interface.
        :type interface_id: str
        :param account_id: The unique identifier of the account.
        :type account_id: str
        :type body: AmsIntegrationAccountUpdateRequest
        :rtype: AmsIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_ams_integration_account_endpoint.call_with_http_info(**kwargs)
