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
from datadog_api_client.v2.model.web_integration_account_update_request import WebIntegrationAccountUpdateRequest


class WebIntegrationsApi:
    """
    Manage web integration accounts programmatically through the Datadog API.
    See the `Web Integrations page <https://app.datadoghq.com/integrations>`_ for more information.
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
        """Create a web integration account.

        Create a new account for a given web integration.

        :param integration_name: The name of the integration (for example, ``databricks`` ).
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
        """Delete a web integration account.

        Delete an account for a given web integration.

        :param integration_name: The name of the integration (for example, ``databricks`` ).
        :type integration_name: str
        :param account_id: The unique identifier of the web integration account.
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
        """Get a web integration account.

        Get a single account for a given web integration.

        :param integration_name: The name of the integration (for example, ``databricks`` ).
        :type integration_name: str
        :param account_id: The unique identifier of the web integration account.
        :type account_id: str
        :rtype: WebIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["account_id"] = account_id

        return self._get_web_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_web_integration_accounts(
        self,
        integration_name: str,
    ) -> WebIntegrationAccountsResponse:
        """List web integration accounts.

        List accounts for a given web integration.

        :param integration_name: The name of the integration (for example, ``databricks`` ).
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
        """Update a web integration account.

        Update an existing account for a given web integration.

        :param integration_name: The name of the integration (for example, ``databricks`` ).
        :type integration_name: str
        :param account_id: The unique identifier of the web integration account.
        :type account_id: str
        :type body: WebIntegrationAccountUpdateRequest
        :rtype: WebIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_name"] = integration_name

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_web_integration_account_endpoint.call_with_http_info(**kwargs)
