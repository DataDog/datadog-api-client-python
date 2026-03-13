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
    from datadog_api_client.v2.model.batch_rows_query_response_data_relationships_rows import (
        BatchRowsQueryResponseDataRelationshipsRows,
    )


class BatchRowsQueryResponseDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_rows_query_response_data_relationships_rows import (
            BatchRowsQueryResponseDataRelationshipsRows,
        )

        return {
            "rows": (BatchRowsQueryResponseDataRelationshipsRows,),
        }

    attribute_map = {
        "rows": "rows",
    }

    def __init__(self_, rows: Union[BatchRowsQueryResponseDataRelationshipsRows, UnsetType] = unset, **kwargs):
        """


        :param rows:
        :type rows: BatchRowsQueryResponseDataRelationshipsRows, optional
        """
        if rows is not unset:
            kwargs["rows"] = rows
        super().__init__(kwargs)
