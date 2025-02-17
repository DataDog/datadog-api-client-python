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
    from datadog_api_client.v1.model.column_order_object import ColumnOrderObject


class ColumnSortObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.column_order_object import ColumnOrderObject

        return {
            "count": (float,),
            "order_by": ([ColumnOrderObject],),
        }

    attribute_map = {
        "count": "count",
        "order_by": "order_by",
    }

    def __init__(
        self_,
        count: Union[float, UnsetType] = unset,
        order_by: Union[List[ColumnOrderObject], UnsetType] = unset,
        **kwargs,
    ):
        """
        Sort object

        :param count: Limit number of items displayed
        :type count: float, optional

        :param order_by: Order criteria
        :type order_by: [ColumnOrderObject], optional
        """
        if count is not unset:
            kwargs["count"] = count
        if order_by is not unset:
            kwargs["order_by"] = order_by
        super().__init__(kwargs)
