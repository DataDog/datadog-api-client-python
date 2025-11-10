# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.table_result_v2_data import TableResultV2Data


class TableResultV2Array(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_result_v2_data import TableResultV2Data

        return {
            "data": ([TableResultV2Data],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[TableResultV2Data], **kwargs):
        """
        List of reference tables.

        :param data: The reference tables.
        :type data: [TableResultV2Data]
        """
        super().__init__(kwargs)

        self_.data = data
