# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.twilio_integration_accounts_response import TwilioIntegrationAccountsResponse
from datadog_api_client.v2.model.twilio_interface_type import TwilioInterfaceType
from datadog_api_client.v2.model.twilio_integration_account_response import TwilioIntegrationAccountResponse
from datadog_api_client.v2.model.twilio_integration_account_request import TwilioIntegrationAccountRequest
from datadog_api_client.v2.model.twilio_integration_account_update_request import TwilioIntegrationAccountUpdateRequest


class TwilioIntegrationAccountsApi:
    """
    Manage Twilio accounts for the Twilio integration, served by the Account Management Service (AMS). The account payload is strongly typed to Twilio; the Twilio interface and its authentication are modeled inline.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/{interface_id}/accounts",
                "operation_id": "create_twilio_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (TwilioInterfaceType,),
                    "attribute": "interface_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (TwilioIntegrationAccountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "delete_twilio_integration_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (TwilioInterfaceType,),
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

        self._get_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "get_twilio_integration_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (TwilioInterfaceType,),
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

        self._list_twilio_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/{interface_id}/accounts",
                "operation_id": "list_twilio_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (TwilioInterfaceType,),
                    "attribute": "interface_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/{interface_id}/accounts/{account_id}",
                "operation_id": "update_twilio_integration_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "interface_id": {
                    "required": True,
                    "openapi_types": (TwilioInterfaceType,),
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
                    "openapi_types": (TwilioIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_twilio_integration_account(
        self,
        interface_id: TwilioInterfaceType,
        body: TwilioIntegrationAccountRequest,
    ) -> TwilioIntegrationAccountResponse:
        """Create a Twilio integration account.

        Create a Twilio integration account for a given interface.

        :param interface_id: Selects the Twilio interface (source-type). Supported values: ``twilio``.
        :type interface_id: TwilioInterfaceType
        :type body: TwilioIntegrationAccountRequest
        :rtype: TwilioIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["body"] = body

        return self._create_twilio_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_twilio_integration_account(
        self,
        interface_id: TwilioInterfaceType,
        account_id: str,
    ) -> None:
        """Delete a Twilio integration account.

        Delete a Twilio integration account.

        :param interface_id: Selects the Twilio interface (source-type). Supported values: ``twilio``.
        :type interface_id: TwilioInterfaceType
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._delete_twilio_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_twilio_integration_account(
        self,
        interface_id: TwilioInterfaceType,
        account_id: str,
    ) -> TwilioIntegrationAccountResponse:
        """Get a Twilio integration account.

        Get a single Twilio integration account.

        :param interface_id: Selects the Twilio interface (source-type). Supported values: ``twilio``.
        :type interface_id: TwilioInterfaceType
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: TwilioIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        return self._get_twilio_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_twilio_integration_accounts(
        self,
        interface_id: TwilioInterfaceType,
    ) -> TwilioIntegrationAccountsResponse:
        """List Twilio integration accounts.

        List the Twilio integration accounts for a given interface.

        :param interface_id: Selects the Twilio interface (source-type). Supported values: ``twilio``.
        :type interface_id: TwilioInterfaceType
        :rtype: TwilioIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        return self._list_twilio_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_twilio_integration_account(
        self,
        interface_id: TwilioInterfaceType,
        account_id: str,
        body: TwilioIntegrationAccountUpdateRequest,
    ) -> TwilioIntegrationAccountResponse:
        """Update a Twilio integration account.

        Update a Twilio integration account. The update is a partial merge: only the fields provided are changed, so a name-only or settings-only update does not need to resend the full payload or write-only credentials.

        :param interface_id: Selects the Twilio interface (source-type). Supported values: ``twilio``.
        :type interface_id: TwilioInterfaceType
        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: TwilioIntegrationAccountUpdateRequest
        :rtype: TwilioIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["interface_id"] = interface_id

        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_twilio_integration_account_endpoint.call_with_http_info(**kwargs)
