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
    from datadog_api_client.v1.model.toplist_widget_legend import ToplistWidgetLegend
    from datadog_api_client.v1.model.toplist_widget_stacked_type import ToplistWidgetStackedType


class ToplistWidgetStacked(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.toplist_widget_legend import ToplistWidgetLegend
        from datadog_api_client.v1.model.toplist_widget_stacked_type import ToplistWidgetStackedType

        return {
            "legend": (ToplistWidgetLegend,),
            "type": (ToplistWidgetStackedType,),
        }

    attribute_map = {
        "legend": "legend",
        "type": "type",
    }

    def __init__(
        self_, type: ToplistWidgetStackedType, legend: Union[ToplistWidgetLegend, UnsetType] = unset, **kwargs
    ):
        """
        Top list widget stacked display options.

        :param legend: Top list widget stacked legend behavior.
        :type legend: ToplistWidgetLegend, optional

        :param type: Top list widget stacked display type.
        :type type: ToplistWidgetStackedType
        """
        if legend is not unset:
            kwargs["legend"] = legend
        super().__init__(kwargs)

        self_.type = type
