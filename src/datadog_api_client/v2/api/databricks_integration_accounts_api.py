# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.databricks_integration_accounts_response import DatabricksIntegrationAccountsResponse
from datadog_api_client.v2.model.databricks_integration_account_response import DatabricksIntegrationAccountResponse
from datadog_api_client.v2.model.databricks_integration_account_create_request import (
    DatabricksIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.databricks_integration_account_update_request import (
    DatabricksIntegrationAccountUpdateRequest,
)


class DatabricksIntegrationAccountsApi:
    """
    Manage your Datadog Databricks integration accounts directly through the Datadog API.
    Create, update, and delete accounts, configure authentication and settings, and
    enable or disable dataflows such as Data Jobs Monitoring, serverless jobs,
    cluster logs, GPU metrics, cloud cost metrics, data observability, and model serving
    metrics. See the
    `Databricks integration page <https://docs.datadoghq.com/integrations/databricks/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_databricks_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (DatabricksIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/databricks/accounts",
                "operation_id": "create_databricks_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DatabricksIntegrationAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_databricks_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/databricks/accounts/{account_id}",
                "operation_id": "delete_databricks_integration_account",
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

        self._get_databricks_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (DatabricksIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/databricks/accounts/{account_id}",
                "operation_id": "get_databricks_integration_account",
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

        self._list_databricks_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (DatabricksIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/databricks/accounts",
                "operation_id": "list_databricks_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_databricks_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (DatabricksIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/databricks/accounts/{account_id}",
                "operation_id": "update_databricks_integration_account",
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
                    "openapi_types": (DatabricksIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_databricks_integration_account(
        self,
        body: DatabricksIntegrationAccountCreateRequest,
    ) -> DatabricksIntegrationAccountResponse:
        """Create a Databricks integration account.

        Create a Databricks integration account.

        :type body: DatabricksIntegrationAccountCreateRequest
        :rtype: DatabricksIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_databricks_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_databricks_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a Databricks integration account.

        Delete a Databricks integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_databricks_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_databricks_integration_account(
        self,
        account_id: str,
    ) -> DatabricksIntegrationAccountResponse:
        """Get a Databricks integration account.

        Get a Databricks integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: DatabricksIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_databricks_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_databricks_integration_accounts(
        self,
    ) -> DatabricksIntegrationAccountsResponse:
        """List Databricks integration accounts.

        List Databricks integration accounts.

        :rtype: DatabricksIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_databricks_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_databricks_integration_account(
        self,
        account_id: str,
        body: DatabricksIntegrationAccountUpdateRequest,
    ) -> DatabricksIntegrationAccountResponse:
        """Update a Databricks integration account.

        Update a Databricks integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: DatabricksIntegrationAccountUpdateRequest
        :rtype: DatabricksIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_databricks_integration_account_endpoint.call_with_http_info(**kwargs)
