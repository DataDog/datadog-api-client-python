# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.get_all_powerpacks_response import GetAllPowerpacksResponse
from datadog_api_client.v2.model.powerpack_response import PowerpackResponse
from datadog_api_client.v2.model.powerpack import Powerpack


class PowerpackApi:
    """
    The powerpack endpoints allow you to:

    * Get a powerpack
    * Create a powerpack
    * Delete a powerpack
    * Get a list of all powerpacks

    The Patch and Delete API methods can only be performed on a powerpack by
    a user who has the powerpack create permission for that specific powerpack.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_powerpack_endpoint = _Endpoint(
            settings={
                "response_type": (PowerpackResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/powerpacks",
                "operation_id": "create_powerpack",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Powerpack,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_powerpack_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/powerpacks/{powerpack_id}",
                "operation_id": "delete_powerpack",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "powerpack_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "powerpack_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_all_powerpacks_endpoint = _Endpoint(
            settings={
                "response_type": (GetAllPowerpacksResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/powerpacks",
                "operation_id": "get_all_powerpacks",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_powerpack_endpoint = _Endpoint(
            settings={
                "response_type": (PowerpackResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/powerpacks/{powerpack_id}",
                "operation_id": "get_powerpack",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "powerpack_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "powerpack_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_powerpack_endpoint = _Endpoint(
            settings={
                "response_type": (PowerpackResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/powerpacks/{powerpack_id}",
                "operation_id": "update_powerpack",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "powerpack_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "powerpack_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Powerpack,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_powerpack(
        self,
        body: Powerpack,
    ) -> PowerpackResponse:
        """Create a new powerpack.

        Create a powerpack.

        :param body: Create a powerpack request body.
        :type body: Powerpack
        :rtype: PowerpackResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_powerpack_endpoint.call_with_http_info(**kwargs)

    def delete_powerpack(
        self,
        powerpack_id: str,
    ) -> None:
        """Delete a powerpack.

        Delete a powerpack.

        :param powerpack_id: Powerpack id
        :type powerpack_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["powerpack_id"] = powerpack_id

        return self._delete_powerpack_endpoint.call_with_http_info(**kwargs)

    def get_all_powerpacks(
        self,
    ) -> GetAllPowerpacksResponse:
        """Get all powerpacks.

        Get a list of all powerpacks.

        :rtype: GetAllPowerpacksResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_all_powerpacks_endpoint.call_with_http_info(**kwargs)

    def get_powerpack(
        self,
        powerpack_id: str,
    ) -> PowerpackResponse:
        """Get a Powerpack.

        Get a powerpack.

        :param powerpack_id: ID of the powerpack.
        :type powerpack_id: str
        :rtype: PowerpackResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["powerpack_id"] = powerpack_id

        return self._get_powerpack_endpoint.call_with_http_info(**kwargs)

    def update_powerpack(
        self,
        powerpack_id: str,
        body: Powerpack,
    ) -> PowerpackResponse:
        """Update a powerpack.

        Update a powerpack.

        :param powerpack_id: ID of the powerpack.
        :type powerpack_id: str
        :param body: Update a powerpack request body.
        :type body: Powerpack
        :rtype: PowerpackResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["powerpack_id"] = powerpack_id

        kwargs["body"] = body

        return self._update_powerpack_endpoint.call_with_http_info(**kwargs)
