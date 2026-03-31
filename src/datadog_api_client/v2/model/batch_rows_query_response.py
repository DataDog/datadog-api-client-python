# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.batch_rows_query_response_data import BatchRowsQueryResponseData


class BatchRowsQueryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_rows_query_response_data import BatchRowsQueryResponseData

        return {
            "data": (BatchRowsQueryResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[BatchRowsQueryResponseData, UnsetType] = unset, **kwargs):
        """
        Response object for a batch rows query against a reference table.

        :param data: Data object for a batch rows query response.
        :type data: BatchRowsQueryResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
