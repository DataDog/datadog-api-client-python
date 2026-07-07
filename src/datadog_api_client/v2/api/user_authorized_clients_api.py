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
from datadog_api_client.v2.model.user_authorized_clients_response import UserAuthorizedClientsResponse
from datadog_api_client.v2.model.user_authorized_client_data import UserAuthorizedClientData
from datadog_api_client.v2.model.user_authorized_client_response import UserAuthorizedClientResponse


class UserAuthorizedClientsApi:
    """
    Manage OAuth2 client authorizations at the user level.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_user_authorized_client_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/user_authorized_clients/{user_authorized_client_id}",
                "operation_id": "delete_user_authorized_client",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "user_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_authorized_client_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_user_authorized_clients_by_client_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/user_authorized_clients/client/{client_id}",
                "operation_id": "delete_user_authorized_clients_by_client",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "client_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_user_authorized_client_endpoint = _Endpoint(
            settings={
                "response_type": (UserAuthorizedClientResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/user_authorized_clients/{user_authorized_client_id}",
                "operation_id": "get_user_authorized_client",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "user_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_authorized_client_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_user_authorized_clients_endpoint = _Endpoint(
            settings={
                "response_type": (UserAuthorizedClientsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/user_authorized_clients",
                "operation_id": "list_user_authorized_clients",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_disabled": {
                    "openapi_types": (str,),
                    "attribute": "filter[disabled]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def delete_user_authorized_client(
        self,
        user_authorized_client_id: str,
    ) -> None:
        """Delete a user authorized client.

        Disable the current user's authorization for the specified OAuth2 client.

        :param user_authorized_client_id: The ID of the user authorized client.
        :type user_authorized_client_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_authorized_client_id"] = user_authorized_client_id

        return self._delete_user_authorized_client_endpoint.call_with_http_info(**kwargs)

    def delete_user_authorized_clients_by_client(
        self,
        client_id: str,
    ) -> None:
        """Delete all user authorized clients for a client.

        Disable all authorizations the current user has granted to the specified OAuth2 client.

        :param client_id: The ID of the OAuth2 client.
        :type client_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["client_id"] = client_id

        return self._delete_user_authorized_clients_by_client_endpoint.call_with_http_info(**kwargs)

    def get_user_authorized_client(
        self,
        user_authorized_client_id: str,
    ) -> UserAuthorizedClientResponse:
        """Get a user authorized client.

        Get a single OAuth2 client authorization for the current user.

        :param user_authorized_client_id: The ID of the user authorized client.
        :type user_authorized_client_id: str
        :rtype: UserAuthorizedClientResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["user_authorized_client_id"] = user_authorized_client_id

        return self._get_user_authorized_client_endpoint.call_with_http_info(**kwargs)

    def list_user_authorized_clients(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_disabled: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> UserAuthorizedClientsResponse:
        """List user authorized clients.

        Get a list of all OAuth2 clients authorized by the current user.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param filter: Filter results by client name, app title, or app description.
        :type filter: str, optional
        :param filter_disabled: Filter results by the user-level disabled status.
        :type filter_disabled: str, optional
        :param include: Comma-separated list of related resources to include. Options: ``oauth2_client`` , ``oauth2_client.app``.
        :type include: str, optional
        :rtype: UserAuthorizedClientsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if include is not unset:
            kwargs["include"] = include

        return self._list_user_authorized_clients_endpoint.call_with_http_info(**kwargs)

    def list_user_authorized_clients_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_disabled: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[UserAuthorizedClientData]:
        """List user authorized clients.

        Provide a paginated version of :meth:`list_user_authorized_clients`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param filter: Filter results by client name, app title, or app description.
        :type filter: str, optional
        :param filter_disabled: Filter results by the user-level disabled status.
        :type filter_disabled: str, optional
        :param include: Comma-separated list of related resources to include. Options: ``oauth2_client`` , ``oauth2_client.app``.
        :type include: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[UserAuthorizedClientData]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if include is not unset:
            kwargs["include"] = include

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_user_authorized_clients_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "page_start": 0,
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
