# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_powerpacks_response import ListPowerpacksResponse
from datadog_api_client.v2.model.powerpack_data import PowerpackData
from datadog_api_client.v2.model.powerpack_response import PowerpackResponse
from datadog_api_client.v2.model.powerpack import Powerpack


class PowerpackApi:
    """
    The Powerpack endpoints allow you to:

    * Get a Powerpack
    * Create a Powerpack
    * Delete a Powerpack
    * Get a list of all Powerpacks

    The Patch and Delete API methods can only be performed on a Powerpack by
    a user who has the powerpack create permission for that specific Powerpack.

    Read `Scale Graphing Expertise with Powerpacks <https://docs.datadoghq.com/dashboards/guide/powerpacks-best-practices/>`_ for more information.
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

        self._list_powerpacks_endpoint = _Endpoint(
            settings={
                "response_type": (ListPowerpacksResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/powerpacks",
                "operation_id": "list_powerpacks",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
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

    def list_powerpacks(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> ListPowerpacksResponse:
        """Get all powerpacks.

        Get a list of all powerpacks.

        :param page_limit: Maximum number of powerpacks in the response.
        :type page_limit: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :rtype: ListPowerpacksResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_powerpacks_endpoint.call_with_http_info(**kwargs)

    def list_powerpacks_with_pagination(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[PowerpackData]:
        """Get all powerpacks.

        Provide a paginated version of :meth:`list_powerpacks`, returning all items.

        :param page_limit: Maximum number of powerpacks in the response.
        :type page_limit: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[PowerpackData]
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 25)
        endpoint = self._list_powerpacks_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

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
