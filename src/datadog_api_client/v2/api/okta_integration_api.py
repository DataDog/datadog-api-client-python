# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.okta_accounts_response import OktaAccountsResponse
from datadog_api_client.v2.model.okta_account_response import OktaAccountResponse
from datadog_api_client.v2.model.okta_account_request import OktaAccountRequest
from datadog_api_client.v2.model.okta_account_update_request import OktaAccountUpdateRequest


class OktaIntegrationApi:
    """
    Configure your `Datadog Okta integration <https://docs.datadoghq.com/integrations/okta/>`_ directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_okta_account_endpoint = _Endpoint(
            settings={
                "response_type": (OktaAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/okta/accounts",
                "operation_id": "create_okta_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OktaAccountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_okta_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/okta/accounts/{account_id}",
                "operation_id": "delete_okta_account",
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

        self._get_okta_account_endpoint = _Endpoint(
            settings={
                "response_type": (OktaAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/okta/accounts/{account_id}",
                "operation_id": "get_okta_account",
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

        self._list_okta_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (OktaAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/okta/accounts",
                "operation_id": "list_okta_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_okta_account_endpoint = _Endpoint(
            settings={
                "response_type": (OktaAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/okta/accounts/{account_id}",
                "operation_id": "update_okta_account",
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
                    "openapi_types": (OktaAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_okta_account(
        self,
        body: OktaAccountRequest,
    ) -> OktaAccountResponse:
        """Add Okta account.

        Create an Okta account.

        :type body: OktaAccountRequest
        :rtype: OktaAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_okta_account_endpoint.call_with_http_info(**kwargs)

    def delete_okta_account(
        self,
        account_id: str,
    ) -> None:
        """Delete Okta account.

        Delete an Okta account.

        :param account_id: None
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_okta_account_endpoint.call_with_http_info(**kwargs)

    def get_okta_account(
        self,
        account_id: str,
    ) -> OktaAccountResponse:
        """Get Okta account.

        Get an Okta account.

        :param account_id: None
        :type account_id: str
        :rtype: OktaAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_okta_account_endpoint.call_with_http_info(**kwargs)

    def list_okta_accounts(
        self,
    ) -> OktaAccountsResponse:
        """List Okta accounts.

        List Okta accounts.

        :rtype: OktaAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_okta_accounts_endpoint.call_with_http_info(**kwargs)

    def update_okta_account(
        self,
        account_id: str,
        body: OktaAccountUpdateRequest,
    ) -> OktaAccountResponse:
        """Update Okta account.

        Update an Okta account.

        :param account_id: None
        :type account_id: str
        :type body: OktaAccountUpdateRequest
        :rtype: OktaAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_okta_account_endpoint.call_with_http_info(**kwargs)
