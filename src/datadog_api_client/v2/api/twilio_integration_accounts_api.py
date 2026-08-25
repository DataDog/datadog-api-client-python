# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.twilio_integration_accounts_response import TwilioIntegrationAccountsResponse
from datadog_api_client.v2.model.twilio_integration_account_response import TwilioIntegrationAccountResponse
from datadog_api_client.v2.model.twilio_integration_account_create_request import TwilioIntegrationAccountCreateRequest
from datadog_api_client.v2.model.twilio_integration_account_update_request import TwilioIntegrationAccountUpdateRequest


class TwilioIntegrationAccountsApi:
    """
    Manage your Datadog Twilio integration accounts directly through the Datadog API.
    Create, update, and delete accounts, configure authentication and settings, and
    enable or disable dataflows such as message logs, event logs, alerts, call
    summaries, and Cloud Cost Management metrics. See the
    `Twilio integration page <https://docs.datadoghq.com/integrations/twilio/>`_ for
    more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/twilio/accounts",
                "operation_id": "create_twilio_integration_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TwilioIntegrationAccountCreateRequest,),
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
                "endpoint_path": "/api/v2/integration-interfaces/twilio/accounts/{account_id}",
                "operation_id": "delete_twilio_integration_account",
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

        self._get_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/twilio/accounts/{account_id}",
                "operation_id": "get_twilio_integration_account",
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

        self._list_twilio_integration_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/twilio/accounts",
                "operation_id": "list_twilio_integration_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_twilio_integration_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioIntegrationAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration-interfaces/twilio/accounts/{account_id}",
                "operation_id": "update_twilio_integration_account",
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
                    "openapi_types": (TwilioIntegrationAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_twilio_integration_account(
        self,
        body: TwilioIntegrationAccountCreateRequest,
    ) -> TwilioIntegrationAccountResponse:
        """Create a Twilio integration account.

        Create a Twilio integration account.

        :type body: TwilioIntegrationAccountCreateRequest
        :rtype: TwilioIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_twilio_integration_account_endpoint.call_with_http_info(**kwargs)

    def delete_twilio_integration_account(
        self,
        account_id: str,
    ) -> None:
        """Delete a Twilio integration account.

        Delete a Twilio integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._delete_twilio_integration_account_endpoint.call_with_http_info(**kwargs)

    def get_twilio_integration_account(
        self,
        account_id: str,
    ) -> TwilioIntegrationAccountResponse:
        """Get a Twilio integration account.

        Get a Twilio integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: TwilioIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_twilio_integration_account_endpoint.call_with_http_info(**kwargs)

    def list_twilio_integration_accounts(
        self,
    ) -> TwilioIntegrationAccountsResponse:
        """List Twilio integration accounts.

        List Twilio integration accounts.

        :rtype: TwilioIntegrationAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_twilio_integration_accounts_endpoint.call_with_http_info(**kwargs)

    def update_twilio_integration_account(
        self,
        account_id: str,
        body: TwilioIntegrationAccountUpdateRequest,
    ) -> TwilioIntegrationAccountResponse:
        """Update a Twilio integration account.

        Update a Twilio integration account. Only the fields provided are changed.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: TwilioIntegrationAccountUpdateRequest
        :rtype: TwilioIntegrationAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_twilio_integration_account_endpoint.call_with_http_info(**kwargs)
