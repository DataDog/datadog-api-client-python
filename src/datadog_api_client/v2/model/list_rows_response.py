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
    from datadog_api_client.v2.model.table_row_resource_data import TableRowResourceData
    from datadog_api_client.v2.model.list_rows_response_links import ListRowsResponseLinks
    from datadog_api_client.v2.model.list_rows_response_meta import ListRowsResponseMeta


class ListRowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_row_resource_data import TableRowResourceData
        from datadog_api_client.v2.model.list_rows_response_links import ListRowsResponseLinks
        from datadog_api_client.v2.model.list_rows_response_meta import ListRowsResponseMeta

        return {
            "data": ([TableRowResourceData],),
            "links": (ListRowsResponseLinks,),
            "meta": (ListRowsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[TableRowResourceData],
        links: ListRowsResponseLinks,
        meta: Union[ListRowsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Paginated list of reference table rows.

        :param data: The rows.
        :type data: [TableRowResourceData]

        :param links: Pagination links for the list rows response.
        :type links: ListRowsResponseLinks

        :param meta: Contains pagination details, including the continuation token for fetching additional rows.
        :type meta: ListRowsResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
