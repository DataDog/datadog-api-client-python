# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.statuspage_account_response import StatuspageAccountResponse
from datadog_api_client.v2.model.statuspage_account_update_request import StatuspageAccountUpdateRequest
from datadog_api_client.v2.model.statuspage_account_create_request import StatuspageAccountCreateRequest
from datadog_api_client.v2.model.statuspage_url_settings_response import StatuspageUrlSettingsResponse
from datadog_api_client.v2.model.statuspage_url_setting_response import StatuspageUrlSettingResponse
from datadog_api_client.v2.model.statuspage_url_setting_create_request import StatuspageUrlSettingCreateRequest
from datadog_api_client.v2.model.statuspage_url_setting_update_request import StatuspageUrlSettingUpdateRequest


class StatuspageIntegrationApi:
    """
    Configure your `Datadog Statuspage integration <https://docs.datadoghq.com/integrations/statuspage/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_statuspage_account_endpoint = _Endpoint(
            settings={
                "response_type": (StatuspageAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/account",
                "operation_id": "create_statuspage_account",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (StatuspageAccountCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_statuspage_url_setting_endpoint = _Endpoint(
            settings={
                "response_type": (StatuspageUrlSettingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/url_settings",
                "operation_id": "create_statuspage_url_setting",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (StatuspageUrlSettingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_statuspage_account_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/account",
                "operation_id": "delete_statuspage_account",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_statuspage_url_setting_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/url_settings/{statuspage_url_setting_id}",
                "operation_id": "delete_statuspage_url_setting",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "statuspage_url_setting_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "statuspage_url_setting_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_statuspage_account_endpoint = _Endpoint(
            settings={
                "response_type": (StatuspageAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/account",
                "operation_id": "get_statuspage_account",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_statuspage_url_settings_endpoint = _Endpoint(
            settings={
                "response_type": (StatuspageUrlSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/url_settings",
                "operation_id": "list_statuspage_url_settings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_statuspage_account_endpoint = _Endpoint(
            settings={
                "response_type": (StatuspageAccountResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/account",
                "operation_id": "update_statuspage_account",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (StatuspageAccountUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_statuspage_url_setting_endpoint = _Endpoint(
            settings={
                "response_type": (StatuspageUrlSettingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/statuspage/url_settings/{statuspage_url_setting_id}",
                "operation_id": "update_statuspage_url_setting",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "statuspage_url_setting_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "statuspage_url_setting_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (StatuspageUrlSettingUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_statuspage_account(
        self,
        body: StatuspageAccountCreateRequest,
    ) -> StatuspageAccountResponse:
        """Create the Statuspage account.

        Create a Statuspage account for your organization. Only one Statuspage
        account can be configured per organization.

        :param body: Statuspage account payload.
        :type body: StatuspageAccountCreateRequest
        :rtype: StatuspageAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_statuspage_account_endpoint.call_with_http_info(**kwargs)

    def create_statuspage_url_setting(
        self,
        body: StatuspageUrlSettingCreateRequest,
    ) -> StatuspageUrlSettingResponse:
        """Create a Statuspage URL setting.

        Create a Statuspage URL setting for your organization.

        :param body: Statuspage URL setting payload.
        :type body: StatuspageUrlSettingCreateRequest
        :rtype: StatuspageUrlSettingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_statuspage_url_setting_endpoint.call_with_http_info(**kwargs)

    def delete_statuspage_account(
        self,
    ) -> None:
        """Delete the Statuspage account.

        Delete the Statuspage account configured for your organization.

        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        return self._delete_statuspage_account_endpoint.call_with_http_info(**kwargs)

    def delete_statuspage_url_setting(
        self,
        statuspage_url_setting_id: str,
    ) -> None:
        """Delete a Statuspage URL setting.

        Delete a single Statuspage URL setting from your organization.

        :param statuspage_url_setting_id: The UUID of the Statuspage URL setting.
        :type statuspage_url_setting_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["statuspage_url_setting_id"] = statuspage_url_setting_id

        return self._delete_statuspage_url_setting_endpoint.call_with_http_info(**kwargs)

    def get_statuspage_account(
        self,
    ) -> StatuspageAccountResponse:
        """Get the Statuspage account.

        Get the Statuspage account configured for your organization.

        :rtype: StatuspageAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_statuspage_account_endpoint.call_with_http_info(**kwargs)

    def list_statuspage_url_settings(
        self,
    ) -> StatuspageUrlSettingsResponse:
        """Get all Statuspage URL settings.

        Get all Statuspage URL settings configured for your organization.

        :rtype: StatuspageUrlSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_statuspage_url_settings_endpoint.call_with_http_info(**kwargs)

    def update_statuspage_account(
        self,
        body: StatuspageAccountUpdateRequest,
    ) -> StatuspageAccountResponse:
        """Update the Statuspage account.

        Update the Statuspage account configured for your organization.

        :param body: Statuspage account payload.
        :type body: StatuspageAccountUpdateRequest
        :rtype: StatuspageAccountResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_statuspage_account_endpoint.call_with_http_info(**kwargs)

    def update_statuspage_url_setting(
        self,
        statuspage_url_setting_id: str,
        body: StatuspageUrlSettingUpdateRequest,
    ) -> StatuspageUrlSettingResponse:
        """Update a Statuspage URL setting.

        Update a single Statuspage URL setting in your organization.

        :param statuspage_url_setting_id: The UUID of the Statuspage URL setting.
        :type statuspage_url_setting_id: str
        :param body: Statuspage URL setting payload.
        :type body: StatuspageUrlSettingUpdateRequest
        :rtype: StatuspageUrlSettingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["statuspage_url_setting_id"] = statuspage_url_setting_id

        kwargs["body"] = body

        return self._update_statuspage_url_setting_endpoint.call_with_http_info(**kwargs)
