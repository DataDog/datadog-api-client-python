# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.query_users_request_data_attributes_sort import QueryUsersRequestDataAttributesSort


class QueryUsersRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_users_request_data_attributes_sort import (
            QueryUsersRequestDataAttributesSort,
        )

        return {
            "limit": (int,),
            "query": (str,),
            "select_columns": ([str],),
            "sort": (QueryUsersRequestDataAttributesSort,),
            "wildcard_search_term": (str,),
        }

    attribute_map = {
        "limit": "limit",
        "query": "query",
        "select_columns": "select_columns",
        "sort": "sort",
        "wildcard_search_term": "wildcard_search_term",
    }

    def __init__(
        self_,
        limit: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        select_columns: Union[List[str], UnsetType] = unset,
        sort: Union[QueryUsersRequestDataAttributesSort, UnsetType] = unset,
        wildcard_search_term: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for filtering and shaping the user query results.

        :param limit: Maximum number of user records to return in the response.
        :type limit: int, optional

        :param query: Filter expression using user attribute conditions to narrow results.
            Filter timestamp attributes such as ``first_seen`` or ``last_seen`` with Unix timestamps in milliseconds, for
            example
            ``first_seen:>=1793750400000`` or ``first_seen:[1793750400000 TO 1794355200000]`` , or with offsets in
            milliseconds
            relative to now, for example ``first_seen:[-604800000 TO 0]`` for the last 7 days. A range needs an upper
            bound.
            Date strings such as ``2026-10-26T00:00:00Z`` are not supported, because their colons break the query syntax.
        :type query: str, optional

        :param select_columns: List of user attribute column names to include in the response.
        :type select_columns: [str], optional

        :param sort: Sorting configuration specifying the field and direction for ordering user query results.
        :type sort: QueryUsersRequestDataAttributesSort, optional

        :param wildcard_search_term: Free-text term used for wildcard search across user attribute values.
        :type wildcard_search_term: str, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if query is not unset:
            kwargs["query"] = query
        if select_columns is not unset:
            kwargs["select_columns"] = select_columns
        if sort is not unset:
            kwargs["sort"] = sort
        if wildcard_search_term is not unset:
            kwargs["wildcard_search_term"] = wildcard_search_term
        super().__init__(kwargs)
