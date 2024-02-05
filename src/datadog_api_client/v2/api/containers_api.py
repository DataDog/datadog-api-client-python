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
from datadog_api_client.v2.model.containers_response import ContainersResponse
from datadog_api_client.v2.model.container_item import ContainerItem


class ContainersApi:
    """
    The Containers API allows you to query container data for your organization. See the `Container Monitoring page <https://docs.datadoghq.com/containers/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_containers_endpoint = _Endpoint(
            settings={
                "response_type": (ContainersResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/containers",
                "operation_id": "list_containers",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "group_by": {
                    "openapi_types": (str,),
                    "attribute": "group_by",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 10000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_containers(
        self,
        *,
        filter_tags: Union[str, UnsetType] = unset,
        group_by: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> ContainersResponse:
        """Get All Containers.

        Get all containers for your organization.

        :param filter_tags: Comma-separated list of tags to filter containers by.
        :type filter_tags: str, optional
        :param group_by: Comma-separated list of tags to group containers by.
        :type group_by: str, optional
        :param sort: Attribute to sort containers by.
        :type sort: str, optional
        :param page_size: Maximum number of results returned.
        :type page_size: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in ``meta.pagination.next_cursor``.
        :type page_cursor: str, optional
        :rtype: ContainersResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if group_by is not unset:
            kwargs["group_by"] = group_by

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._list_containers_endpoint.call_with_http_info(**kwargs)

    def list_containers_with_pagination(
        self,
        *,
        filter_tags: Union[str, UnsetType] = unset,
        group_by: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[ContainerItem]:
        """Get All Containers.

        Provide a paginated version of :meth:`list_containers`, returning all items.

        :param filter_tags: Comma-separated list of tags to filter containers by.
        :type filter_tags: str, optional
        :param group_by: Comma-separated list of tags to group containers by.
        :type group_by: str, optional
        :param sort: Attribute to sort containers by.
        :type sort: str, optional
        :param page_size: Maximum number of results returned.
        :type page_size: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in ``meta.pagination.next_cursor``.
        :type page_cursor: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[ContainerItem]
        """
        kwargs: Dict[str, Any] = {}
        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if group_by is not unset:
            kwargs["group_by"] = group_by

        if sort is not unset:
            kwargs["sort"] = sort

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        local_page_size = get_attribute_from_path(kwargs, "page_size", 1000)
        endpoint = self._list_containers_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.pagination.next_cursor",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
