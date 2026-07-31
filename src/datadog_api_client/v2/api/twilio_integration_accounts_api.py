# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.twilio_accounts_response import TwilioAccountsResponse
from datadog_api_client.v2.model.twilio_account_response import TwilioAccountResponse
from datadog_api_client.v2.model.twilio_account_request import TwilioAccountRequest
from datadog_api_client.v2.model.twilio_account_update_request import TwilioAccountUpdateRequest


class TwilioIntegrationAccountsApi:
    """
    Manage Twilio accounts for the Twilio ``twilio`` interface, served by the Account Management Service (AMS). Concrete, strongly typed CRUD operations for the single Twilio interface.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_twilio_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/twilio/accounts",
                "operation_id": "create_twilio_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TwilioAccountRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_twilio_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/twilio/accounts/{account_id}",
                "operation_id": "delete_twilio_account",
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

        self._get_twilio_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/twilio/accounts/{account_id}",
                "operation_id": "get_twilio_account",
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

        self._list_twilio_accounts_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioAccountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/twilio/accounts",
                "operation_id": "list_twilio_accounts",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_twilio_account_endpoint = _Endpoint(
            settings={
                "response_type": (TwilioAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integrations/twilio/interfaces/twilio/accounts/{account_id}",
                "operation_id": "update_twilio_account",
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
                    "openapi_types": (TwilioAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_twilio_account(
        self,
        body: TwilioAccountRequest,
    ) -> TwilioAccountResponse:
        """Create a Twilio integration account.

        Create a Twilio integration account.

        :type body: TwilioAccountRequest
        :rtype: TwilioAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_twilio_account_endpoint.call_with_http_info(**kwargs)

    def delete_twilio_account(
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

        return self._delete_twilio_account_endpoint.call_with_http_info(**kwargs)

    def get_twilio_account(
        self,
        account_id: str,
    ) -> TwilioAccountResponse:
        """Get a Twilio integration account.

        Get a single Twilio integration account.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :rtype: TwilioAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        return self._get_twilio_account_endpoint.call_with_http_info(**kwargs)

    def list_twilio_accounts(
        self,
    ) -> TwilioAccountsResponse:
        """List Twilio integration accounts.

        List the Twilio integration accounts.

        :rtype: TwilioAccountsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_twilio_accounts_endpoint.call_with_http_info(**kwargs)

    def update_twilio_account(
        self,
        account_id: str,
        body: TwilioAccountUpdateRequest,
    ) -> TwilioAccountResponse:
        """Update a Twilio integration account.

        Update a Twilio integration account. The update is a partial merge: only the fields provided are changed, so a name-only or settings-only update does not need to resend the full payload or write-only credentials.

        :param account_id: Unique identifier of the integration account.
        :type account_id: str
        :type body: TwilioAccountUpdateRequest
        :rtype: TwilioAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["account_id"] = account_id

        kwargs["body"] = body

        return self._update_twilio_account_endpoint.call_with_http_info(**kwargs)
