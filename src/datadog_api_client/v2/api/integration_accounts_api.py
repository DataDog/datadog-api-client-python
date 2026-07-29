# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.integration_accounts_response import IntegrationAccountsResponse
from datadog_api_client.v2.model.integration_account_integration_id import IntegrationAccountIntegrationId
from datadog_api_client.v2.model.integration_account_interface_id import IntegrationAccountInterfaceId
from datadog_api_client.v2.model.integration_account_response import IntegrationAccountResponse
from datadog_api_client.v2.model.integration_account_request import IntegrationAccountRequest
from datadog_api_client.v2.model.integration_account_update_request import IntegrationAccountUpdateRequest


class IntegrationAccountsApi:
    """
    Manage accounts for Datadog integrations served by the Account Management Service (AMS). The account payload is strongly typed per integration and interface.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (IntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_id}/interfaces/{interface_id}/accounts",
                "operation_id": "create_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountIntegrationId,),
                    "attribute": "integration_id",
                    "location": "path",
                },
                "interface_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IntegrationAccountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_id}/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "delete_integration_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountIntegrationId,),
                    "attribute": "integration_id",
                    "location": "path",
                },
                "interface_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountInterfaceId,),
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

        self._get_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (IntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_id}/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "get_integration_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountIntegrationId,),
                    "attribute": "integration_id",
                    "location": "path",
                },
                "interface_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountInterfaceId,),
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

        self._list_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (IntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_id}/interfaces/{interface_id}/accounts",
                "operation_id": "list_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountIntegrationId,),
                    "attribute": "integration_id",
                    "location": "path",
                },
                "interface_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountInterfaceId,),
                    "attribute": "interface_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (IntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/{integration_id}/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "update_integration_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "integration_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountIntegrationId,),
                    "attribute": "integration_id",
                    "location": "path",
                },
                "interface_id": {
                    "required": True,
                    "openapi_types": (IntegrationAccountInterfaceId,),
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
                    "openapi_types": (IntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_integration_account(
        self,
        integration_id: IntegrationAccountIntegrationId,
        interface_id: IntegrationAccountInterfaceId,
        body: IntegrationAccountRequest,
    ) -> IntegrationAccountResponse:
        """Create an integration account.

        Create an integration account for a given integration/interface.

        :param integration_id: Grouping/RBAC scope. Selects the integration whose accounts are addressed.
        :type integration_id: IntegrationAccountIntegrationId
        :param interface_id: Selects the interface (source-type) within the integration.
        :type interface_id: IntegrationAccountInterfaceId
        :type body: IntegrationAccountRequest
        :rtype: IntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        kwargs["interface_id"] = interface_id

        kwargs["body"] = body

        return self._create_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_integration_account(
        self,
        integration_id: IntegrationAccountIntegrationId,
        interface_id: IntegrationAccountInterfaceId,
        account_id: str,
    ) -> None:
        """Delete an integration account.

        Delete an integration account.

        :param integration_id: Grouping/RBAC scope. Selects the integration whose accounts are addressed.
        :type integration_id: IntegrationAccountIntegrationId
        :param interface_id: Selects the interface (source-type) within the integration.
        :type interface_id: IntegrationAccountInterfaceId
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._delete_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_integration_account(
        self,
        integration_id: IntegrationAccountIntegrationId,
        interface_id: IntegrationAccountInterfaceId,
        account_id: str,
    ) -> IntegrationAccountResponse:
        """Get an integration account.

        Get a single integration account.

        :param integration_id: Grouping/RBAC scope. Selects the integration whose accounts are addressed.
        :type integration_id: IntegrationAccountIntegrationId
        :param interface_id: Selects the interface (source-type) within the integration.
        :type interface_id: IntegrationAccountInterfaceId
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: IntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._get_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_integration_accounts(
        self,
        integration_id: IntegrationAccountIntegrationId,
        interface_id: IntegrationAccountInterfaceId,
    ) -> IntegrationAccountsResponse:
        """List integration accounts.

        List the integration accounts for a given integration/interface.

        :param integration_id: Grouping/RBAC scope. Selects the integration whose accounts are addressed.
        :type integration_id: IntegrationAccountIntegrationId
        :param interface_id: Selects the interface (source-type) within the integration.
        :type interface_id: IntegrationAccountInterfaceId
        :rtype: IntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        kwargs["interface_id"] = interface_id

        return self._list_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_integration_account(
        self,
        integration_id: IntegrationAccountIntegrationId,
        interface_id: IntegrationAccountInterfaceId,
        account_id: str,
        body: IntegrationAccountUpdateRequest,
    ) -> IntegrationAccountResponse:
        """Update an integration account.

        Update an integration account. The update is a partial merge: only the fields provided are changed, so a name-only or settings-only update does not need to resend the full integration payload or write-only credentials. When present, ``type`` selects the integration/interface variant. Top-level attributes and the contents of ``authentication`` and ``settings`` are merged one level deep; the ``dataflows`` array is merged by ``id``.

        :param integration_id: Grouping/RBAC scope. Selects the integration whose accounts are addressed.
        :type integration_id: IntegrationAccountIntegrationId
        :param interface_id: Selects the interface (source-type) within the integration.
        :type interface_id: IntegrationAccountInterfaceId
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: IntegrationAccountUpdateRequest
        :rtype: IntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["integration_id"] = integration_id

        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_integration_account_endpoint.call_with_http_info(**kwargs)
