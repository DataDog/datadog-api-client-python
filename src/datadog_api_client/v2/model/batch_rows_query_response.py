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
    from datadog_api_client.v2.model.batch_rows_query_response_data import BatchRowsQueryResponseData
    from datadog_api_client.v2.model.table_row_resource_data import TableRowResourceData


class BatchRowsQueryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_rows_query_response_data import BatchRowsQueryResponseData
        from datadog_api_client.v2.model.table_row_resource_data import TableRowResourceData

        return {
            "data": (BatchRowsQueryResponseData,),
            "included": ([TableRowResourceData],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[BatchRowsQueryResponseData, UnsetType] = unset,
        included: Union[List[TableRowResourceData], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object for a batch rows query against a reference table.

        :param data: Data object for a batch rows query response.
        :type data: BatchRowsQueryResponseData, optional

        :param included: Full row resources matching the query, included alongside the relationship references in ``data``.
        :type included: [TableRowResourceData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
