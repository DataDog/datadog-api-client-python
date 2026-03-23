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
    from datadog_api_client.v2.model.table_row_resource_identifier import TableRowResourceIdentifier


class BatchDeleteRowsRequestArray(ModelNormal):
    validations = {
        "data": {
            "max_items": 200,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_row_resource_identifier import TableRowResourceIdentifier

        return {
            "data": ([TableRowResourceIdentifier],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[TableRowResourceIdentifier], **kwargs):
        """
        The request body for deleting multiple rows from a reference table.

        :param data: List of row resources to delete from the reference table.
        :type data: [TableRowResourceIdentifier]
        """
        super().__init__(kwargs)

        self_.data = data
