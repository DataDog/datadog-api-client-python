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
    from datadog_api_client.v1.model.column_order_object_order import ColumnOrderObjectOrder
    from datadog_api_client.v1.model.column_order_object_type import ColumnOrderObjectType


class ColumnOrderObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.column_order_object_order import ColumnOrderObjectOrder
        from datadog_api_client.v1.model.column_order_object_type import ColumnOrderObjectType

        return {
            "index": (float,),
            "name": (str,),
            "order": (ColumnOrderObjectOrder,),
            "type": (ColumnOrderObjectType,),
        }

    attribute_map = {
        "index": "index",
        "name": "name",
        "order": "order",
        "type": "type",
    }

    def __init__(
        self_,
        order: ColumnOrderObjectOrder,
        type: ColumnOrderObjectType,
        index: Union[float, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Order criteria

        :param index: Index of the sorted column
        :type index: float, optional

        :param name: Name of the sorted column
        :type name: str, optional

        :param order: Order object
        :type order: ColumnOrderObjectOrder

        :param type: type of column
        :type type: ColumnOrderObjectType
        """
        if index is not unset:
            kwargs["index"] = index
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.order = order
        self_.type = type
