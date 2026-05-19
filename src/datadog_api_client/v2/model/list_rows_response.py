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
    from datadog_api_client.v2.model.table_row_resource_data import TableRowResourceData
    from datadog_api_client.v2.model.list_rows_response_links import ListRowsResponseLinks


class ListRowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_row_resource_data import TableRowResourceData
        from datadog_api_client.v2.model.list_rows_response_links import ListRowsResponseLinks

        return {
            "data": ([TableRowResourceData],),
            "links": (ListRowsResponseLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(self_, data: List[TableRowResourceData], links: ListRowsResponseLinks, **kwargs):
        """
        Paginated list of reference table rows.

        :param data: The rows.
        :type data: [TableRowResourceData]

        :param links: Pagination links for the list rows response.
        :type links: ListRowsResponseLinks
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
