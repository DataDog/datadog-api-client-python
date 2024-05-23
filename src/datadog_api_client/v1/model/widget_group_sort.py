# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.widget_sort import WidgetSort
    from datadog_api_client.v1.model.group_type import GroupType


class WidgetGroupSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort import WidgetSort
        from datadog_api_client.v1.model.group_type import GroupType

        return {
            "name": (str,),
            "order": (WidgetSort,),
            "type": (GroupType,),
        }

    attribute_map = {
        "name": "name",
        "order": "order",
        "type": "type",
    }

    def __init__(self_, name: str, order: WidgetSort, type: GroupType, **kwargs):
        """
        The group to sort the widget by.

        :param name: The name of the group.
        :type name: str

        :param order: Widget sorting methods.
        :type order: WidgetSort

        :param type: Set the sort type to group.
        :type type: GroupType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.order = order
        self_.type = type
