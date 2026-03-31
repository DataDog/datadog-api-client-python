# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class BatchRowsQueryRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "row_ids": ([str],),
            "table_id": (str,),
        }

    attribute_map = {
        "row_ids": "row_ids",
        "table_id": "table_id",
    }

    def __init__(self_, row_ids: List[str], table_id: str, **kwargs):
        """
        Attributes for a batch rows query request.

        :param row_ids: List of row identifiers to query from the reference table.
        :type row_ids: [str]

        :param table_id: Unique identifier of the reference table to query.
        :type table_id: str
        """
        super().__init__(kwargs)

        self_.row_ids = row_ids
        self_.table_id = table_id
