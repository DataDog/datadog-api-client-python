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
    from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query import (
        QueryEventFilteredUsersRequestDataAttributesEventQuery,
    )


class QueryEventFilteredUsersRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_event_filtered_users_request_data_attributes_event_query import (
            QueryEventFilteredUsersRequestDataAttributesEventQuery,
        )

        return {
            "event_query": (QueryEventFilteredUsersRequestDataAttributesEventQuery,),
            "include_row_count": (bool,),
            "limit": (int,),
            "query": (str,),
            "select_columns": ([str],),
        }

    attribute_map = {
        "event_query": "event_query",
        "include_row_count": "include_row_count",
        "limit": "limit",
        "query": "query",
        "select_columns": "select_columns",
    }

    def __init__(
        self_,
        event_query: Union[QueryEventFilteredUsersRequestDataAttributesEventQuery, UnsetType] = unset,
        include_row_count: Union[bool, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        select_columns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param event_query:
        :type event_query: QueryEventFilteredUsersRequestDataAttributesEventQuery, optional

        :param include_row_count:
        :type include_row_count: bool, optional

        :param limit:
        :type limit: int, optional

        :param query:
        :type query: str, optional

        :param select_columns:
        :type select_columns: [str], optional
        """
        if event_query is not unset:
            kwargs["event_query"] = event_query
        if include_row_count is not unset:
            kwargs["include_row_count"] = include_row_count
        if limit is not unset:
            kwargs["limit"] = limit
        if query is not unset:
            kwargs["query"] = query
        if select_columns is not unset:
            kwargs["select_columns"] = select_columns
        super().__init__(kwargs)
