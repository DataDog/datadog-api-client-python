# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.snowflake_integration_accounts_response import SnowflakeIntegrationAccountsResponse
from datadog_api_client.v2.model.snowflake_integration_account_response import SnowflakeIntegrationAccountResponse
from datadog_api_client.v2.model.snowflake_integration_account_create_request import (
    SnowflakeIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.snowflake_integration_account_update_request import (
    SnowflakeIntegrationAccountUpdateRequest,
)


class SnowflakeIntegrationApi:
    """
    Manage your Datadog Snowflake integration accounts and account resources directly
    through the Datadog API. See the
    `Snowflake integration page <https://docs.datadoghq.com/integrations/snowflake_web/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_snowflake_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (SnowflakeIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/snowflake/accounts",
                "operation_id": "create_snowflake_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SnowflakeIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_snowflake_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/snowflake/accounts/{account_id}",
                "operation_id": "delete_snowflake_integration_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
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

        self._get_snowflake_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (SnowflakeIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/snowflake/accounts/{account_id}",
                "operation_id": "get_snowflake_integration_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
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

        self._list_snowflake_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (SnowflakeIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/snowflake/accounts",
                "operation_id": "list_snowflake_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_snowflake_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (SnowflakeIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/snowflake/accounts/{account_id}",
                "operation_id": "update_snowflake_integration_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "account_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "account_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SnowflakeIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_snowflake_integration_account(
        self,
        body: SnowflakeIntegrationAccountCreateRequest,
    ) -> SnowflakeIntegrationAccountResponse:
        """Create a Snowflake integration account.

        Create a Snowflake integration account.

        :type body: SnowflakeIntegrationAccountCreateRequest
        :rtype: SnowflakeIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_snowflake_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_snowflake_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a Snowflake integration account.

        Delete a Snowflake integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_snowflake_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_snowflake_integration_account(
        self,
        account_id: str,
    ) -> SnowflakeIntegrationAccountResponse:
        """Get a Snowflake integration account.

        Get a Snowflake integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: SnowflakeIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_snowflake_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_snowflake_integration_accounts(
        self,
    ) -> SnowflakeIntegrationAccountsResponse:
        """List Snowflake integration accounts.

        List Snowflake integration accounts.

        :rtype: SnowflakeIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_snowflake_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_snowflake_integration_account(
        self,
        account_id: str,
        body: SnowflakeIntegrationAccountUpdateRequest,
    ) -> SnowflakeIntegrationAccountResponse:
        """Update a Snowflake integration account.

        Update a Snowflake integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: SnowflakeIntegrationAccountUpdateRequest
        :rtype: SnowflakeIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_snowflake_integration_account_endpoint.call_with_http_info(**kwargs)
