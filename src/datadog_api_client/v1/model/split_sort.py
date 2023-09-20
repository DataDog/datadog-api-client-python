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
    from datadog_api_client.v1.model.split_config_sort_compute import SplitConfigSortCompute
    from datadog_api_client.v1.model.widget_sort import WidgetSort


class SplitSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.split_config_sort_compute import SplitConfigSortCompute
        from datadog_api_client.v1.model.widget_sort import WidgetSort

        return {
            "compute": (SplitConfigSortCompute,),
            "order": (WidgetSort,),
        }

    attribute_map = {
        "compute": "compute",
        "order": "order",
    }

    def __init__(self_, order: WidgetSort, compute: Union[SplitConfigSortCompute, UnsetType] = unset, **kwargs):
        """
        Controls the order in which graphs appear in the split.

        :param compute: Defines the metric and aggregation used as the sort value.
        :type compute: SplitConfigSortCompute, optional

        :param order: Widget sorting methods.
        :type order: WidgetSort
        """
        if compute is not unset:
            kwargs["compute"] = compute
        super().__init__(kwargs)

        self_.order = order
