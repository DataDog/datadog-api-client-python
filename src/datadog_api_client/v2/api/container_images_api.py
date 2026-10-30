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
from datadog_api_client.v2.model.container_images_response import ContainerImagesResponse
from datadog_api_client.v2.model.container_image_item import ContainerImageItem


class ContainerImagesApi:
    """
    The Container Images API allows you to query Container Image data for your organization. See the `Container Images View page <https://docs.datadoghq.com/infrastructure/containers/container_images/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_container_images_endpoint = _Endpoint(
            settings={
                "response_type": (ContainerImagesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/container_images",
                "operation_id": "list_container_images",
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

    def list_container_images(
        self,
        *,
        filter_tags: Union[str, UnsetType] = unset,
        group_by: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> ContainerImagesResponse:
        """Get all Container Images.

        Get all container images for your organization. This endpoint queries current
        inventory and does not support time-range parameters.

        Use ``group_by`` to return image groups with counts. Grouped results are limited
        by ``page[size]`` , may be incomplete, and do not support pagination.

        **Note** : To enrich the data returned by this endpoint with security scans, see the new `api/v2/security/scanned-assets-metadata <https://docs.datadoghq.com/api/latest/security-monitoring/#list-scanned-assets-metadata>`_ endpoint.

        :param filter_tags: Comma-separated ``key:value`` tags. An image must match every tag. Wildcards, negation
            ( ``-key:value`` ), spaces, and ``IN (...)`` are not supported. Use keys such as ``image_registry``
            and ``image_tag``. To match any of several values of the same key, make one request per value.
        :type filter_tags: str, optional
        :param group_by: Comma-separated list of up to three tag keys, such as ``image_registry,image_tag``. Returns
            ``container_image_group`` objects with counts and tags. Grouped results ignore ``sort`` and do
            not support pagination. Images missing a grouping key are excluded. An image with multiple
            values for a grouping tag can appear in multiple groups. Grouped results may be incomplete.
            Compare counts only within the returned groups; they do not establish the most common tags
            or proportions across the inventory. For inventory-wide comparisons, omit ``group_by`` , keep the
            same filters, paginate all results, and deduplicate by returned image ID. For an inventory total,
            use ``meta.pagination.total`` from a query without grouping.
        :type group_by: str, optional
        :param sort: Attribute to sort individual images by, such as ``size`` or ``container_count``.
            Defaults to ``image_name`` in ascending order. Prefix the attribute with ``-`` for
            descending order, such as ``-size``. Ignored when ``group_by`` is specified.
        :type sort: str, optional
        :param page_size: Maximum number of results returned. Grouped queries default to ``100`` , with a maximum of ``1000`` groups.
            Without grouping, queries default to ``1000`` , with a maximum of ``10000`` images. Minimum is ``1``.
        :type page_size: int, optional
        :param page_cursor: Opaque cursor from ``meta.pagination.next_cursor`` for individual images. Keep the same filters
            and sort order. Stop when absent or empty. Grouped queries do not support pagination.
        :type page_cursor: str, optional
        :rtype: ContainerImagesResponse
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

        return self._list_container_images_endpoint.call_with_http_info(**kwargs)

    def list_container_images_with_pagination(
        self,
        *,
        filter_tags: Union[str, UnsetType] = unset,
        group_by: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[ContainerImageItem]:
        """Get all Container Images.

        Provide a paginated version of :meth:`list_container_images`, returning all items.

        :param filter_tags: Comma-separated ``key:value`` tags. An image must match every tag. Wildcards, negation
            ( ``-key:value`` ), spaces, and ``IN (...)`` are not supported. Use keys such as ``image_registry``
            and ``image_tag``. To match any of several values of the same key, make one request per value.
        :type filter_tags: str, optional
        :param group_by: Comma-separated list of up to three tag keys, such as ``image_registry,image_tag``. Returns
            ``container_image_group`` objects with counts and tags. Grouped results ignore ``sort`` and do
            not support pagination. Images missing a grouping key are excluded. An image with multiple
            values for a grouping tag can appear in multiple groups. Grouped results may be incomplete.
            Compare counts only within the returned groups; they do not establish the most common tags
            or proportions across the inventory. For inventory-wide comparisons, omit ``group_by`` , keep the
            same filters, paginate all results, and deduplicate by returned image ID. For an inventory total,
            use ``meta.pagination.total`` from a query without grouping.
        :type group_by: str, optional
        :param sort: Attribute to sort individual images by, such as ``size`` or ``container_count``.
            Defaults to ``image_name`` in ascending order. Prefix the attribute with ``-`` for
            descending order, such as ``-size``. Ignored when ``group_by`` is specified.
        :type sort: str, optional
        :param page_size: Maximum number of results returned. Grouped queries default to ``100`` , with a maximum of ``1000`` groups.
            Without grouping, queries default to ``1000`` , with a maximum of ``10000`` images. Minimum is ``1``.
        :type page_size: int, optional
        :param page_cursor: Opaque cursor from ``meta.pagination.next_cursor`` for individual images. Keep the same filters
            and sort order. Stop when absent or empty. Grouped queries do not support pagination.
        :type page_cursor: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[ContainerImageItem]
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
        endpoint = self._list_container_images_endpoint
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
