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
    from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery


class SegmentPreviewAttributes(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_data_query import SegmentDataQuery

        return {
            "account_store_columns": ([str],),
            "data_query": (SegmentDataQuery,),
            "limit": (int,),
            "reference_table_columns": ([str],),
            "user_store_columns": ([str],),
        }

    attribute_map = {
        "account_store_columns": "account_store_columns",
        "data_query": "data_query",
        "limit": "limit",
        "reference_table_columns": "reference_table_columns",
        "user_store_columns": "user_store_columns",
    }

    def __init__(
        self_,
        data_query: SegmentDataQuery,
        account_store_columns: Union[List[str], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        reference_table_columns: Union[List[str], UnsetType] = unset,
        user_store_columns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Segment definition to preview and the columns to return.
        Without columns, the response returns the user ID, or the account ID for account segments.

        :param account_store_columns: Account profile columns to return.
        :type account_store_columns: [str], optional

        :param data_query: Defines who belongs to the segment. It contains one or more blocks, up to 20 in total.
            Use ``combination`` to combine named blocks with a boolean formula such as ``A AND NOT B``.
        :type data_query: SegmentDataQuery

        :param limit: Maximum number of rows to return, up to 1000. Defaults to 1000.
        :type limit: int, optional

        :param reference_table_columns: Reference table columns to return.
        :type reference_table_columns: [str], optional

        :param user_store_columns: User profile columns to return.
        :type user_store_columns: [str], optional
        """
        if account_store_columns is not unset:
            kwargs["account_store_columns"] = account_store_columns
        if limit is not unset:
            kwargs["limit"] = limit
        if reference_table_columns is not unset:
            kwargs["reference_table_columns"] = reference_table_columns
        if user_store_columns is not unset:
            kwargs["user_store_columns"] = user_store_columns
        super().__init__(kwargs)

        self_.data_query = data_query
