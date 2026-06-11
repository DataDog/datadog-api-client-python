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
from datadog_api_client.v2.model.identity_providers_response import IdentityProvidersResponse
from datadog_api_client.v2.model.identity_provider_response import IdentityProviderResponse
from datadog_api_client.v2.model.identity_provider_update_request import IdentityProviderUpdateRequest
from datadog_api_client.v2.model.users_response import UsersResponse
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.user import User


class IdentityProvidersApi:
    """
    Manage identity providers and user authentication method overrides.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_identity_providers_endpoint = _Endpoint(
            settings={
                "response_type": (IdentityProvidersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/identity_providers",
                "operation_id": "list_identity_providers",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_identity_provider_users_endpoint = _Endpoint(
            settings={
                "response_type": (UsersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/identity_providers/{idp_id}/users",
                "operation_id": "list_identity_provider_users",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "idp_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "idp_id",
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
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "sort_dir": {
                    "openapi_types": (QuerySortOrder,),
                    "attribute": "sort_dir",
                    "location": "query",
                },
                "filter": {
                    "openapi_types": (str,),
                    "attribute": "filter",
                    "location": "query",
                },
                "filter_status": {
                    "openapi_types": (str,),
                    "attribute": "filter[status]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_identity_provider_endpoint = _Endpoint(
            settings={
                "response_type": (IdentityProviderResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/identity_providers/{idp_id}",
                "operation_id": "update_identity_provider",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "idp_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "idp_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (IdentityProviderUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def list_identity_providers(
        self,
    ) -> IdentityProvidersResponse:
        """List identity providers.

        Get all identity providers available for the current organization.

        :rtype: IdentityProvidersResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_identity_providers_endpoint.call_with_http_info(**kwargs)

    def list_identity_provider_users(
        self,
        idp_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        sort_dir: Union[QuerySortOrder, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_status: Union[str, UnsetType] = unset,
    ) -> UsersResponse:
        """List users with an identity provider override.

        Get all users in the organization whose login method has been overridden
        to use the specified identity provider.

        :param idp_id: The ID of the identity provider.
        :type idp_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: User attribute to order results by. Options include ``email`` and ``name``.
        :type sort: str, optional
        :param sort_dir: Direction of sort. Options: ``asc`` , ``desc``.
        :type sort_dir: QuerySortOrder, optional
        :param filter: Filter users by the given string. Defaults to no filtering.
        :type filter: str, optional
        :param filter_status: Filter on status attribute.
            Comma-separated list, with possible values ``Active`` , ``Pending`` , and ``Disabled``.
            Defaults to no filtering.
        :type filter_status: str, optional
        :rtype: UsersResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["idp_id"] = idp_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if sort_dir is not unset:
            kwargs["sort_dir"] = sort_dir

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        return self._list_identity_provider_users_endpoint.call_with_http_info(**kwargs)

    def list_identity_provider_users_with_pagination(
        self,
        idp_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        sort_dir: Union[QuerySortOrder, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        filter_status: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[User]:
        """List users with an identity provider override.

        Provide a paginated version of :meth:`list_identity_provider_users`, returning all items.

        :param idp_id: The ID of the identity provider.
        :type idp_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param sort: User attribute to order results by. Options include ``email`` and ``name``.
        :type sort: str, optional
        :param sort_dir: Direction of sort. Options: ``asc`` , ``desc``.
        :type sort_dir: QuerySortOrder, optional
        :param filter: Filter users by the given string. Defaults to no filtering.
        :type filter: str, optional
        :param filter_status: Filter on status attribute.
            Comma-separated list, with possible values ``Active`` , ``Pending`` , and ``Disabled``.
            Defaults to no filtering.
        :type filter_status: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[User]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["idp_id"] = idp_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if sort is not unset:
            kwargs["sort"] = sort

        if sort_dir is not unset:
            kwargs["sort_dir"] = sort_dir

        if filter is not unset:
            kwargs["filter"] = filter

        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_identity_provider_users_endpoint
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

    def update_identity_provider(
        self,
        idp_id: str,
        body: IdentityProviderUpdateRequest,
    ) -> IdentityProviderResponse:
        """Update an identity provider.

        Enable or disable an identity provider for the current organization.

        :param idp_id: The ID of the identity provider.
        :type idp_id: str
        :type body: IdentityProviderUpdateRequest
        :rtype: IdentityProviderResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["idp_id"] = idp_id

        kwargs["body"] = body

        return self._update_identity_provider_endpoint.call_with_http_info(**kwargs)
