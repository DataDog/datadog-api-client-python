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
from datadog_api_client.v2.model.org_authorized_clients_response import OrgAuthorizedClientsResponse
from datadog_api_client.v2.model.org_authorized_client_data import OrgAuthorizedClientData
from datadog_api_client.v2.model.org_authorized_client_response import OrgAuthorizedClientResponse
from datadog_api_client.v2.model.org_authorized_client_update_request import OrgAuthorizedClientUpdateRequest
from datadog_api_client.v2.model.user_authorized_clients_response import UserAuthorizedClientsResponse
from datadog_api_client.v2.model.org_authorized_client_user_authorizations_sort import (
    OrgAuthorizedClientUserAuthorizationsSort,
)
from datadog_api_client.v2.model.user_authorized_client_data import UserAuthorizedClientData


class OrgAuthorizedClientsApi:
    """
    Manage OAuth2 client authorizations at the organization level.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_org_authorized_client_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients/{org_authorized_client_id}",
                "operation_id": "delete_org_authorized_client",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "org_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_authorized_client_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_org_authorized_client_all_user_authorizations_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients/{org_authorized_client_id}/user/{user_id}",
                "operation_id": "delete_org_authorized_client_all_user_authorizations",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "org_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_authorized_client_id",
                    "location": "path",
                },
                "user_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "user_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_org_authorized_client_user_authorization_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients/{org_authorized_client_id}/user_authorized_clients/{user_authorized_client_id}",
                "operation_id": "delete_org_authorized_client_user_authorization",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "org_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_authorized_client_id",
                    "location": "path",
                },
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

        self._get_org_authorized_client_endpoint = _Endpoint(
            settings={
                "response_type": (OrgAuthorizedClientResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients/{org_authorized_client_id}",
                "operation_id": "get_org_authorized_client",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "org_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_authorized_client_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "filter_user_authorized_clients_disabled": {
                    "openapi_types": (str,),
                    "attribute": "filter[user_authorized_clients][disabled]",
                    "location": "query",
                },
                "filter_user_authorized_clients_user_disabled": {
                    "openapi_types": (str,),
                    "attribute": "filter[user_authorized_clients][user][disabled]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_org_authorized_clients_endpoint = _Endpoint(
            settings={
                "response_type": (OrgAuthorizedClientsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients",
                "operation_id": "list_org_authorized_clients",
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
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_oauth2_client_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[oauth2_client][name]",
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

        self._list_org_authorized_client_user_authorizations_endpoint = _Endpoint(
            settings={
                "response_type": (UserAuthorizedClientsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients/{org_authorized_client_id}/user_authorized_clients",
                "operation_id": "list_org_authorized_client_user_authorizations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "org_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_authorized_client_id",
                    "location": "path",
                },
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
                "sort": {
                    "openapi_types": (OrgAuthorizedClientUserAuthorizationsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "filter_disabled": {
                    "openapi_types": (str,),
                    "attribute": "filter[disabled]",
                    "location": "query",
                },
                "filter_user_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[user][name]",
                    "location": "query",
                },
                "filter_user_email": {
                    "openapi_types": (str,),
                    "attribute": "filter[user][email]",
                    "location": "query",
                },
                "filter_user_disabled": {
                    "openapi_types": (str,),
                    "attribute": "filter[user][disabled]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_org_authorized_client_endpoint = _Endpoint(
            settings={
                "response_type": (OrgAuthorizedClientResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/org_authorized_clients/{org_authorized_client_id}",
                "operation_id": "update_org_authorized_client",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "org_authorized_client_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "org_authorized_client_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OrgAuthorizedClientUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_org_authorized_client(
        self,
        org_authorized_client_id: str,
    ) -> None:
        """Delete an org authorized client.

        Disable an OAuth2 client authorization for the current organization, revoking access for all users.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        return self._delete_org_authorized_client_endpoint.call_with_http_info(**kwargs)

    def delete_org_authorized_client_all_user_authorizations(
        self,
        org_authorized_client_id: str,
        user_id: str,
    ) -> None:
        """Delete a user's authorizations for a client.

        Disable all authorizations for a specific user for the specified OAuth2 client in the current organization.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :param user_id: The ID of the user.
        :type user_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        kwargs["user_id"] = user_id

        return self._delete_org_authorized_client_all_user_authorizations_endpoint.call_with_http_info(**kwargs)

    def delete_org_authorized_client_user_authorization(
        self,
        org_authorized_client_id: str,
        user_authorized_client_id: str,
    ) -> None:
        """Delete a user authorization for a client.

        Disable a specific user authorization for the specified OAuth2 client in the current organization.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :param user_authorized_client_id: The ID of the user authorized client.
        :type user_authorized_client_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        kwargs["user_authorized_client_id"] = user_authorized_client_id

        return self._delete_org_authorized_client_user_authorization_endpoint.call_with_http_info(**kwargs)

    def get_org_authorized_client(
        self,
        org_authorized_client_id: str,
        *,
        include: Union[str, UnsetType] = unset,
        filter_user_authorized_clients_disabled: Union[str, UnsetType] = unset,
        filter_user_authorized_clients_user_disabled: Union[str, UnsetType] = unset,
    ) -> OrgAuthorizedClientResponse:
        """Get an org authorized client.

        Get a single OAuth2 client authorized for the current organization.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :param include: Comma-separated list of related resources to include.
            Options: ``oauth2_client`` , ``oauth2_client.app`` , ``oauth2_client.scopes`` , ``user_authorized_clients.user``.
        :type include: str, optional
        :param filter_user_authorized_clients_disabled: Filter included user authorized clients by disabled status.
        :type filter_user_authorized_clients_disabled: str, optional
        :param filter_user_authorized_clients_user_disabled: Filter included user authorized clients by user disabled status.
        :type filter_user_authorized_clients_user_disabled: str, optional
        :rtype: OrgAuthorizedClientResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        if include is not unset:
            kwargs["include"] = include

        if filter_user_authorized_clients_disabled is not unset:
            kwargs["filter_user_authorized_clients_disabled"] = filter_user_authorized_clients_disabled

        if filter_user_authorized_clients_user_disabled is not unset:
            kwargs["filter_user_authorized_clients_user_disabled"] = filter_user_authorized_clients_user_disabled

        return self._get_org_authorized_client_endpoint.call_with_http_info(**kwargs)

    def list_org_authorized_clients(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_oauth2_client_name: Union[str, UnsetType] = unset,
        filter_disabled: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> OrgAuthorizedClientsResponse:
        """List org authorized clients.

        Get a list of all OAuth2 clients authorized for the current organization.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Field to sort results by. Options include ``oauth2_client.name``.
        :type sort: str, optional
        :param filter: Filter results by client name, app title, or app description.
        :type filter: str, optional
        :param filter_oauth2_client_name: Filter results by the OAuth2 client name.
        :type filter_oauth2_client_name: str, optional
        :param filter_disabled: Filter results by the org-level disabled status.
        :type filter_disabled: str, optional
        :param include: Comma-separated list of related resources to include.
            Options: ``oauth2_client`` , ``oauth2_client.app`` , ``user_authorized_clients.user``.
        :type include: str, optional
        :rtype: OrgAuthorizedClientsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_oauth2_client_name is not unset:
            kwargs["filter_oauth2_client_name"] = filter_oauth2_client_name

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if include is not unset:
            kwargs["include"] = include

        return self._list_org_authorized_clients_endpoint.call_with_http_info(**kwargs)

    def list_org_authorized_clients_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_oauth2_client_name: Union[str, UnsetType] = unset,
        filter_disabled: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[OrgAuthorizedClientData]:
        """List org authorized clients.

        Provide a paginated version of :meth:`list_org_authorized_clients`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Field to sort results by. Options include ``oauth2_client.name``.
        :type sort: str, optional
        :param filter: Filter results by client name, app title, or app description.
        :type filter: str, optional
        :param filter_oauth2_client_name: Filter results by the OAuth2 client name.
        :type filter_oauth2_client_name: str, optional
        :param filter_disabled: Filter results by the org-level disabled status.
        :type filter_disabled: str, optional
        :param include: Comma-separated list of related resources to include.
            Options: ``oauth2_client`` , ``oauth2_client.app`` , ``user_authorized_clients.user``.
        :type include: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[OrgAuthorizedClientData]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_oauth2_client_name is not unset:
            kwargs["filter_oauth2_client_name"] = filter_oauth2_client_name

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if include is not unset:
            kwargs["include"] = include

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_org_authorized_clients_endpoint
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

    def list_org_authorized_client_user_authorizations(
        self,
        org_authorized_client_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[OrgAuthorizedClientUserAuthorizationsSort, UnsetType] = unset,
        filter_disabled: Union[str, UnsetType] = unset,
        filter_user_name: Union[str, UnsetType] = unset,
        filter_user_email: Union[str, UnsetType] = unset,
        filter_user_disabled: Union[str, UnsetType] = unset,
    ) -> UserAuthorizedClientsResponse:
        """List user authorizations for a client.

        Get a list of user authorizations for the specified OAuth2 client in the current organization.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Field to sort results by. Options: ``user.name`` , ``user.email`` , ``oauth2_client.name``.
        :type sort: OrgAuthorizedClientUserAuthorizationsSort, optional
        :param filter_disabled: Filter results by the user authorization disabled status.
        :type filter_disabled: str, optional
        :param filter_user_name: Filter results by user name.
        :type filter_user_name: str, optional
        :param filter_user_email: Filter results by user email.
        :type filter_user_email: str, optional
        :param filter_user_disabled: Filter results by whether the user is disabled.
        :type filter_user_disabled: str, optional
        :rtype: UserAuthorizedClientsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if filter_user_name is not unset:
            kwargs["filter_user_name"] = filter_user_name

        if filter_user_email is not unset:
            kwargs["filter_user_email"] = filter_user_email

        if filter_user_disabled is not unset:
            kwargs["filter_user_disabled"] = filter_user_disabled

        return self._list_org_authorized_client_user_authorizations_endpoint.call_with_http_info(**kwargs)

    def list_org_authorized_client_user_authorizations_with_pagination(
        self,
        org_authorized_client_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[OrgAuthorizedClientUserAuthorizationsSort, UnsetType] = unset,
        filter_disabled: Union[str, UnsetType] = unset,
        filter_user_name: Union[str, UnsetType] = unset,
        filter_user_email: Union[str, UnsetType] = unset,
        filter_user_disabled: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[UserAuthorizedClientData]:
        """List user authorizations for a client.

        Provide a paginated version of :meth:`list_org_authorized_client_user_authorizations`, returning all items.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: Field to sort results by. Options: ``user.name`` , ``user.email`` , ``oauth2_client.name``.
        :type sort: OrgAuthorizedClientUserAuthorizationsSort, optional
        :param filter_disabled: Filter results by the user authorization disabled status.
        :type filter_disabled: str, optional
        :param filter_user_name: Filter results by user name.
        :type filter_user_name: str, optional
        :param filter_user_email: Filter results by user email.
        :type filter_user_email: str, optional
        :param filter_user_disabled: Filter results by whether the user is disabled.
        :type filter_user_disabled: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[UserAuthorizedClientData]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if filter_disabled is not unset:
            kwargs["filter_disabled"] = filter_disabled

        if filter_user_name is not unset:
            kwargs["filter_user_name"] = filter_user_name

        if filter_user_email is not unset:
            kwargs["filter_user_email"] = filter_user_email

        if filter_user_disabled is not unset:
            kwargs["filter_user_disabled"] = filter_user_disabled

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_org_authorized_client_user_authorizations_endpoint
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

    def update_org_authorized_client(
        self,
        org_authorized_client_id: str,
        body: OrgAuthorizedClientUpdateRequest,
    ) -> OrgAuthorizedClientResponse:
        """Update an org authorized client.

        Enable or disable an OAuth2 client authorization for the current organization.

        :param org_authorized_client_id: The ID of the org authorized client.
        :type org_authorized_client_id: str
        :type body: OrgAuthorizedClientUpdateRequest
        :rtype: OrgAuthorizedClientResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["org_authorized_client_id"] = org_authorized_client_id

        kwargs["body"] = body

        return self._update_org_authorized_client_endpoint.call_with_http_info(**kwargs)
