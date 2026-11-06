# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.rum_archive_config_list_response import RumArchiveConfigListResponse
from datadog_api_client.v2.model.rum_archive_config_response import RumArchiveConfigResponse
from datadog_api_client.v2.model.rum_archive_config_upsert_request import RumArchiveConfigUpsertRequest


class RUMManagedArchivesApi:
    """
    Configure Managed Archives for RUM applications. Your organization must have Managed Archives enabled.

    Requires ``rum_rehydration_filter_read`` to list or get configurations, or ``rum_rehydration_filter_write`` to create, update, or delete them.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_rum_archive_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/archive/{app_id}",
                "operation_id": "delete_rum_archive_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rum_archive_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumArchiveConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/archive/{app_id}",
                "operation_id": "get_rum_archive_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_archive_configs_endpoint = _Endpoint(
            settings={
                "response_type": (RumArchiveConfigListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/archive",
                "operation_id": "list_rum_archive_configs",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_number": {
                    "validation": {
                        "inclusive_maximum": 10000,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_archive_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumArchiveConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/archive/{app_id}",
                "operation_id": "update_rum_archive_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "app_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumArchiveConfigUpsertRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_rum_archive_config(
        self,
        app_id: UUID,
    ) -> None:
        """Delete an archive configuration.

        Delete the archive configuration for a RUM application. Archived and recovered session data is not deleted.

        :param app_id: RUM application ID.
        :type app_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._delete_rum_archive_config_endpoint.call_with_http_info(**kwargs)

    def get_rum_archive_config(
        self,
        app_id: UUID,
    ) -> RumArchiveConfigResponse:
        """Get an archive configuration.

        Get the archive configuration for a RUM application.

        :param app_id: RUM application ID.
        :type app_id: UUID
        :rtype: RumArchiveConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._get_rum_archive_config_endpoint.call_with_http_info(**kwargs)

    def list_rum_archive_configs(
        self,
        *,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> RumArchiveConfigListResponse:
        """List archive configurations.

        Get the list of archive configurations for your organization.

        :param page_number: Page number.
        :type page_number: int, optional
        :param page_size: Configurations per page.
        :type page_size: int, optional
        :rtype: RumArchiveConfigListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_rum_archive_configs_endpoint.call_with_http_info(**kwargs)

    def update_rum_archive_config(
        self,
        app_id: UUID,
        body: RumArchiveConfigUpsertRequest,
    ) -> RumArchiveConfigResponse:
        """Create or update an archive configuration.

        Create or update the archive configuration for a RUM application. The application ID in the path must match ``data.id``. Disabling archiving does not delete archived sessions.

        :param app_id: RUM application ID. Must match data.id for PUT.
        :type app_id: UUID
        :param body: JSON:API request body.
        :type body: RumArchiveConfigUpsertRequest
        :rtype: RumArchiveConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        kwargs["body"] = body

        return self._update_rum_archive_config_endpoint.call_with_http_info(**kwargs)
