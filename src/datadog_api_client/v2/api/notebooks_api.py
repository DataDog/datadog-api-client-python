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
)
from datadog_api_client.v2.model.notebook_search_response import NotebookSearchResponse


class NotebooksApi:
    """
    Interact with your notebooks through the API to search and retrieve notebooks.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._search_notebooks_endpoint = _Endpoint(
            settings={
                "response_type": (NotebookSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/notebooks/search",
                "operation_id": "search_notebooks",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "page": {
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "limit": {
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def search_notebooks(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        page: Union[int, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> NotebookSearchResponse:
        """Search notebooks.

        Search for notebooks using a query string.

        :param query: Search query string.
        :type query: str, optional
        :param sort: Sort field for results.
        :type sort: str, optional
        :param include: Additional data to include in the response.
        :type include: str, optional
        :param page: Page number for pagination.
        :type page: int, optional
        :param limit: Maximum number of results to return.
        :type limit: int, optional
        :rtype: NotebookSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if include is not unset:
            kwargs["include"] = include

        if page is not unset:
            kwargs["page"] = page

        if limit is not unset:
            kwargs["limit"] = limit

        return self._search_notebooks_endpoint.call_with_http_info(**kwargs)
