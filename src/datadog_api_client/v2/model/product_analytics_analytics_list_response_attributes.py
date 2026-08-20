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
    from datadog_api_client.v2.model.product_analytics_analytics_list_record import ProductAnalyticsAnalyticsListRecord


class ProductAnalyticsAnalyticsListResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_analytics_list_record import (
            ProductAnalyticsAnalyticsListRecord,
        )

        return {
            "records": ([ProductAnalyticsAnalyticsListRecord],),
            "total_count": (int,),
        }

    attribute_map = {
        "records": "records",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        records: Union[List[ProductAnalyticsAnalyticsListRecord], UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an analytics list response, containing the matching event rows.

        :param records: The event rows, each holding the values of the requested columns.
        :type records: [ProductAnalyticsAnalyticsListRecord], optional

        :param total_count: Total number of records matching the query, before the row limit is applied.
        :type total_count: int, optional
        """
        if records is not unset:
            kwargs["records"] = records
        if total_count is not unset:
            kwargs["total_count"] = total_count
        super().__init__(kwargs)
