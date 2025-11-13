# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.team_connection_delete_request import TeamConnectionDeleteRequest
from datadog_api_client.v2.model.team_connections_response import TeamConnectionsResponse
from datadog_api_client.v2.model.team_connection import TeamConnection
from datadog_api_client.v2.model.team_connection_create_request import TeamConnectionCreateRequest


class TeamConnectionsApi:
    """
    View and manage relationships between Datadog teams and teams from external sources, such as GitHub.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_team_connections_endpoint = _Endpoint(
            settings={
                "response_type": (TeamConnectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/connections",
                "operation_id": "create_team_connections",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamConnectionCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_team_connections_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/connections",
                "operation_id": "delete_team_connections",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TeamConnectionDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_team_connections_endpoint = _Endpoint(
            settings={
                "response_type": (TeamConnectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/team/connections",
                "operation_id": "list_team_connections",
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
                "filter_sources": {
                    "openapi_types": ([str],),
                    "attribute": "filter[sources]",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_team_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[team_ids]",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_connected_team_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[connected_team_ids]",
                    "location": "query",
                    "collection_format": "csv",
                },
                "filter_connection_ids": {
                    "openapi_types": ([str],),
                    "attribute": "filter[connection_ids]",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_team_connections(
        self,
        body: TeamConnectionCreateRequest,
    ) -> TeamConnectionsResponse:
        """Create team connections.

        Create multiple team connections.

        :type body: TeamConnectionCreateRequest
        :rtype: TeamConnectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_team_connections_endpoint.call_with_http_info(**kwargs)

    def delete_team_connections(
        self,
        body: TeamConnectionDeleteRequest,
    ) -> None:
        """Delete team connections.

        Delete multiple team connections.

        :type body: TeamConnectionDeleteRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_team_connections_endpoint.call_with_http_info(**kwargs)

    def list_team_connections(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_sources: Union[List[str], UnsetType] = unset,
        filter_team_ids: Union[List[str], UnsetType] = unset,
        filter_connected_team_ids: Union[List[str], UnsetType] = unset,
        filter_connection_ids: Union[List[str], UnsetType] = unset,
    ) -> TeamConnectionsResponse:
        """List team connections.

        Returns all team connections.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param filter_sources: Filter team connections by external source systems.
        :type filter_sources: [str], optional
        :param filter_team_ids: Filter team connections by Datadog team IDs.
        :type filter_team_ids: [str], optional
        :param filter_connected_team_ids: Filter team connections by connected team IDs from external systems.
        :type filter_connected_team_ids: [str], optional
        :param filter_connection_ids: Filter team connections by connection IDs.
        :type filter_connection_ids: [str], optional
        :rtype: TeamConnectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_sources is not unset:
            kwargs["filter_sources"] = filter_sources

        if filter_team_ids is not unset:
            kwargs["filter_team_ids"] = filter_team_ids

        if filter_connected_team_ids is not unset:
            kwargs["filter_connected_team_ids"] = filter_connected_team_ids

        if filter_connection_ids is not unset:
            kwargs["filter_connection_ids"] = filter_connection_ids

        return self._list_team_connections_endpoint.call_with_http_info(**kwargs)

    def list_team_connections_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        filter_sources: Union[List[str], UnsetType] = unset,
        filter_team_ids: Union[List[str], UnsetType] = unset,
        filter_connected_team_ids: Union[List[str], UnsetType] = unset,
        filter_connection_ids: Union[List[str], UnsetType] = unset,
    ) -> collections.abc.Iterable[TeamConnection]:
        """List team connections.

        Provide a paginated version of :meth:`list_team_connections`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :param filter_sources: Filter team connections by external source systems.
        :type filter_sources: [str], optional
        :param filter_team_ids: Filter team connections by Datadog team IDs.
        :type filter_team_ids: [str], optional
        :param filter_connected_team_ids: Filter team connections by connected team IDs from external systems.
        :type filter_connected_team_ids: [str], optional
        :param filter_connection_ids: Filter team connections by connection IDs.
        :type filter_connection_ids: [str], optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[TeamConnection]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if filter_sources is not unset:
            kwargs["filter_sources"] = filter_sources

        if filter_team_ids is not unset:
            kwargs["filter_team_ids"] = filter_team_ids

        if filter_connected_team_ids is not unset:
            kwargs["filter_connected_team_ids"] = filter_connected_team_ids

        if filter_connection_ids is not unset:
            kwargs["filter_connection_ids"] = filter_connection_ids

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_team_connections_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_param": "page_number",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
