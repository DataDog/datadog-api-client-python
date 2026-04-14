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
    from datadog_api_client.v1.model.widget_sort import WidgetSort


class ProductAnalyticsFunnelGroupBySort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort import WidgetSort

        return {
            "aggregation": (str,),
            "metric": (str,),
            "order": (WidgetSort,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "metric": "metric",
        "order": "order",
    }

    def __init__(
        self_,
        aggregation: str,
        metric: Union[str, UnsetType] = unset,
        order: Union[WidgetSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sort configuration for user journey funnel group by.

        :param aggregation: Aggregation type.
        :type aggregation: str

        :param metric: Metric to sort by.
        :type metric: str, optional

        :param order: Widget sorting methods.
        :type order: WidgetSort, optional
        """
        if metric is not unset:
            kwargs["metric"] = metric
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)

        self_.aggregation = aggregation
