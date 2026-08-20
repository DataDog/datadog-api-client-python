# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_retention_quota_scope_type import RumRetentionQuotaScopeType
from datadog_api_client.v2.model.rum_retention_quota_config_response import RumRetentionQuotaConfigResponse
from datadog_api_client.v2.model.rum_retention_quota_config_update_request import RumRetentionQuotaConfigUpdateRequest


class RUMRetentionQuotaApi:
    """
    Manage RUM retention quota configurations for your organization's RUM applications.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_rum_quota_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/retention-quota/{scope_type}/{scope_id}",
                "operation_id": "delete_rum_quota_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "scope_type": {
                    "required": True,
                    "openapi_types": (RumRetentionQuotaScopeType,),
                    "attribute": "scope_type",
                    "location": "path",
                },
                "scope_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "scope_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rum_quota_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionQuotaConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/retention-quota/{scope_type}/{scope_id}",
                "operation_id": "get_rum_quota_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "scope_type": {
                    "required": True,
                    "openapi_types": (RumRetentionQuotaScopeType,),
                    "attribute": "scope_type",
                    "location": "path",
                },
                "scope_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "scope_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._upsert_rum_quota_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumRetentionQuotaConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/retention-quota/{scope_type}/{scope_id}",
                "operation_id": "upsert_rum_quota_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "scope_type": {
                    "required": True,
                    "openapi_types": (RumRetentionQuotaScopeType,),
                    "attribute": "scope_type",
                    "location": "path",
                },
                "scope_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "scope_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumRetentionQuotaConfigUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_rum_quota_config(
        self,
        scope_type: RumRetentionQuotaScopeType,
        scope_id: str,
    ) -> None:
        """Delete a RUM retention quota configuration.

        Delete the RUM retention quota configuration for a given scope.

        :param scope_type: The type of scope the retention quota configuration applies to.
        :type scope_type: RumRetentionQuotaScopeType
        :param scope_id: The identifier of the scope the retention quota configuration applies to.
            For the ``application`` scope, this is the RUM application ID.
        :type scope_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["scope_type"] = scope_type

        kwargs["scope_id"] = scope_id

        return self._delete_rum_quota_config_endpoint.call_with_http_info(**kwargs)

    def get_rum_quota_config(
        self,
        scope_type: RumRetentionQuotaScopeType,
        scope_id: str,
    ) -> RumRetentionQuotaConfigResponse:
        """Get a RUM retention quota configuration.

        Get the RUM retention quota configuration for a given scope.

        :param scope_type: The type of scope the retention quota configuration applies to.
        :type scope_type: RumRetentionQuotaScopeType
        :param scope_id: The identifier of the scope the retention quota configuration applies to.
            For the ``application`` scope, this is the RUM application ID.
        :type scope_id: str
        :rtype: RumRetentionQuotaConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["scope_type"] = scope_type

        kwargs["scope_id"] = scope_id

        return self._get_rum_quota_config_endpoint.call_with_http_info(**kwargs)

    def upsert_rum_quota_config(
        self,
        scope_type: RumRetentionQuotaScopeType,
        scope_id: str,
        body: RumRetentionQuotaConfigUpdateRequest,
    ) -> RumRetentionQuotaConfigResponse:
        """Create or update a RUM retention quota config.

        Create or update the RUM retention quota configuration for a given scope.
        Returns the retention quota configuration object when the request is successful.

        :param scope_type: The type of scope the retention quota configuration applies to.
        :type scope_type: RumRetentionQuotaScopeType
        :param scope_id: The identifier of the scope the retention quota configuration applies to.
            For the ``application`` scope, this is the RUM application ID.
        :type scope_id: str
        :param body: The definition of the RUM retention quota configuration to create or update.
        :type body: RumRetentionQuotaConfigUpdateRequest
        :rtype: RumRetentionQuotaConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["scope_type"] = scope_type

        kwargs["scope_id"] = scope_id

        kwargs["body"] = body

        return self._upsert_rum_quota_config_endpoint.call_with_http_info(**kwargs)
