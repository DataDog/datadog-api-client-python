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
    from datadog_api_client.v2.model.query_account_request_data_attributes_sort import (
        QueryAccountRequestDataAttributesSort,
    )


class QueryAccountRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_account_request_data_attributes_sort import (
            QueryAccountRequestDataAttributesSort,
        )

        return {
            "limit": (int,),
            "query": (str,),
            "select_columns": ([str],),
            "sort": (QueryAccountRequestDataAttributesSort,),
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
        sort: Union[QueryAccountRequestDataAttributesSort, UnsetType] = unset,
        wildcard_search_term: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param limit:
        :type limit: int, optional

        :param query:
        :type query: str, optional

        :param select_columns:
        :type select_columns: [str], optional

        :param sort:
        :type sort: QueryAccountRequestDataAttributesSort, optional

        :param wildcard_search_term:
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
